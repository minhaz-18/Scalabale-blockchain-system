from pycoin.convention.tx_fee import TX_FEE_PER_THOUSAND_BYTES
from pycoin.tx.tx_utils import create_tx, sign_tx

DUST = 0

class Wallet(object):

    def __init__(self, wallet_storage_context, keychain, desired_spendable_count=None):
        self.wallet_storage_context = wallet_storage_context
        self.keychain = keychain
        self._last_block_index = 0
        self._desired_spendable_count = desired_spendable_count

    def __enter__(self):
        self.wallet_storage_context.lock()
        return self.wallet_storage_context

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.wallet_storage_context.commit()
        self.wallet_storage_context.unlock()

    def create_unsigned_send_tx(self, address, amount):
        total_input_value = 0
        estimated_fee = TX_FEE_PER_THOUSAND_BYTES
        with self as context:
            spendables = []
            for spendable in context.spendables():
                spendables.append(spendable)
                total_input_value += spendable.coin_value
                if total_input_value >= amount + estimated_fee:
                    break
            else:
                raise ValueError("insufficient funds: only %d available" % total_input_value)

            # mark the given spendables as "unconfirmed_spent"
            for spendable in spendables:
                context.update_does_seem_spent(spendable.tx_hash, spendable.tx_out_index, does_seem_spent=True)

            payables = [(address, amount)]
            change_amount = total_input_value - estimated_fee - amount
            if change_amount > DUST:
                change_address = self.keychain.get_change_address()
                payables.append(change_address)

            if self._desired_spendable_count is not None:
                if context.spendable_count() < self._desired_spendable_count:
                    if change_amount > 2 * DUST:
                        change_address = self.keychain.get_change_address()
                        payables.append(change_address)

            tx = create_tx(spendables, payables, fee=estimated_fee)
            context.commit()
        return tx

    # for collecting spendables
    def got_mempool_tx_callback(self, tx):
        with self as context:
            for tx_in in tx.txs_in:
                context.update_does_seem_spent(tx_in.previous_hash, tx_in.previous_index, does_seem_spent=True)
            for spendable in tx.tx_outs_as_spendable():
                if self.keychain.is_spendable_interesting(spendable):
                    context.create_spendable(spendable)
            context.commit()

    def _process_confirmed_tx(self, context, tx, blockheader, block_index):
        for tx_in in tx.txs_in:
            context.update_block_index_spent(tx_in.previous_hash, tx_in.previous_index, block_index)
        for spendable in tx.tx_outs_as_spendable():
            if self.keychain.is_spendable_interesting(spendable):
                spendable.block_index_available = block_index
                context.create_spendable(spendable)

    def _add_block(self, blockheader, block_index, txs):
        with self as context:
            context.note_added_block(blockheader, block_index)
            for tx in txs:
                self._process_confirmed_tx(context, tx, blockheader, block_index)
            context.commit()

    def _rollback_block(self, blockheader, block_index):
        with self as context:
            context.note_rollback_block(blockheader, block_index)
            context.commit()

    def get_balance(self, confirmations=1):
        with self as context:
            return context.get_balance(confirmations)

    def got_ops_callback(self, ops):
        for op, blockheader, block_index, txs in ops:
            if op == 'add':
                self._add_block(blockheader, block_index, txs)
                self._last_block_index = block_index
            elif op == 'remove':
                self._rollback_block(blockheader, block_index)
                self._last_block_index = block_index - 1
            else:
                raise Exception("unknown op: %s" % op)
