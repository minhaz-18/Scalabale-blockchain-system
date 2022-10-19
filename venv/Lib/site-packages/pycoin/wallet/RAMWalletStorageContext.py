from .WalletStorageContext import WalletStorageContext


class RAMWalletStorageContext(WalletStorageContext):
    def __init__(self):
        self.spendable_list = []
        self.idx_by_hash_index = {}
        self.last_block_index = -1

    def lock(self):
        self.ops = []

    def unlock(self):
        self.ops = []

    def commit(self):
        for op in self.ops:
            op()
        self.ops = []

    def rollback(self):
        self.ops = []

    def create_spendable(self, spendable):
        the_pair = (spendable.tx_hash, spendable.tx_out_index)
        def f():
            if the_pair in self.idx_by_hash_index:
                spendable_idx = len(self.spendable_list)
                s = self.spendable_list[self.idx_by_hash_index[the_pair]]
                s.block_index_available = spendable.block_index_available
                s.does_seem_spent = spendable.does_seem_spent
                s.block_index_spent = spendable.block_index_spent
            else:
                spendable_idx = len(self.spendable_list)
                self.idx_by_hash_index[the_pair] = spendable_idx
                self.spendable_list.append(spendable)

        self.ops.append(f)

    def update_block_index_available(self, previous_hash, previous_index, block_index):
        """
        If this Spendable is in the DB, mark it as unconfirmed_spent.
        """
        spendable_idx = self.idx_by_hash_index.get((previous_hash, previous_index))
        if spendable_idx is None:
            return

        def f():
            self.spendable_list[spendable_idx].block_index_available = block_index
            if block_index is not None:
                self.spendable_list[spendable_idx].block_index_available = block_index

        self.ops.append(f)

    def update_does_seem_spent(self, previous_hash, previous_index, does_seem_spent):
        """
        If this Spendable is in the DB, mark it as unconfirmed_spent.
        """
        spendable_idx = self.idx_by_hash_index.get((previous_hash, previous_index))
        if spendable_idx is None:
            return

        def f():
            self.spendable_list[spendable_idx].does_seem_spent = does_seem_spent

        self.ops.append(f)

    def update_block_index_spent(self, previous_hash, previous_index, block_index):
        """
        If this Spendable is in the DB, mark it as unconfirmed_spent.
        """
        spendable_idx = self.idx_by_hash_index.get((previous_hash, previous_index))
        if spendable_idx is None:
            return

        def f():
            self.spendable_list[spendable_idx].block_index_spent = block_index
            if block_index is not None:
                self.spendable_list[spendable_idx].block_index_spent = block_index

        self.ops.append(f)

    def note_added_block(self, block, block_index):
        def f():
            self.last_block_index = block_index
        self.ops.append(f)

    def note_rollback_block(self, block, block_index):
        for spendable in self.spendable_list:

            if spendable.block_index_spent == block_index:

                def f1():
                    spendable.block_index_spent = None

                self.ops.append(f1)

            if spendable.block_index_available == block_index:

                def f2():
                    spendable.block_index_available = None

                self.ops.append(f2)

        def f():
            self.last_block_index = block_index - 1
        self.ops.append(f)

    # for spending
    def spendables(self, include_unconfirmed=False):
        for s in self.spendable_list:
            if not include_unconfirmed:
                if s.block_index_available is None or s.does_seem_spent:
                    continue
            yield s

    def __str__(self):
        return str("%d: %s" % (self.last_block_index, self.spendable_list))
