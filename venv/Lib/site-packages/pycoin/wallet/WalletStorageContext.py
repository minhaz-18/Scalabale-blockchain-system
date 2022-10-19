
class WalletStorageContext(object):

    def lock(self):
        pass

    def unlock(self):
        pass

    def commit(self):
        raise NotImplementedError()

    def rollback(self):
        raise NotImplementedError()

    # here are some methods that need to be overwritten in subclasses
    def create_spendable(self, spendable):
        """
        Record this Spendable.
        """
        raise NotImplementedError()

    def update_block_index_available(self, previous_hash, previous_index, block_index):
        """
        If this Spendable is in the DB, mark it as unconfirmed_spent.
        """
        raise NotImplementedError()

    def update_does_seem_spent(self, previous_hash, previous_index, does_seem_spent):
        """
        If this Spendable is in the DB, mark it as unconfirmed_spent.
        """
        raise NotImplementedError()

    def update_block_index_spent(self, previous_hash, previous_index, block_index_spent):
        """
        If this Spendable is in the DB, mark it as unconfirmed_spent.
        """
        raise NotImplementedError()

    # these methods MIGHT need to be overwritten
    def note_added_block(self, block, block_index):
        pass

    def note_rollback_block(self, block, block_index):
        pass

    def get_balance(self, confirmations=1):
        balance = 0
        for s in self.spendables(confirmations=confirmations):
            # if it looks already spent, skip
            if s.does_seem_spent:
                continue
            if confirmations > 0:
                # if unconfirmed and we want confirmations, skip
                if s.block_index_available is None:
                    continue
                # if not enough confirmations have elapsed, skip
                if self.last_block_index() - s.block_index_available + 1 < confirmations:
                    continue
            balance += s.coin_value
        return balance

    # for spending
    def spendables(self, include_unconfirmed=False):
        raise NotImplementedError()

    def spendable_count(self):
        return sum(1 for s in self.spendables()
                   if s.block_index_available is not None
                   and not s.does_seem_spent
                   and s.block_index_spent is None)
