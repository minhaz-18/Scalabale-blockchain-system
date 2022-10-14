from ..tx import Spendable
from .RAMWalletStorageContext import RAMWalletStorageContext


class FileWalletStorageContext(RAMWalletStorageContext):
    def __init__(self, path="/tmp/spendables.db.txt"):
        super(FileWalletStorageContext, self).__init__()
        self.spendable_list = []
        self.idx_by_hash_index = {}
        self.path = path
        self.last_block_index = 0
        try:
            with open(self.path) as f:
                self.last_block_index = int(f.readline()[:-1])
                for l in f:
                    spendable = Spendable.from_text(l)
                    self.idx_by_hash_index[(spendable.tx_hash, spendable.tx_out_index)] = \
                        len(self.spendable_list)
                    self.spendable_list.append(spendable)
        except Exception as ex:
            pass

    def commit(self):
        for op in self.ops:
            op()
        if len(self.ops) > 0:
            self.flush_db()
        self.ops = []

    def flush_db(self):
        f = open(self.path, "w")
        f.write("%d\n" % self.last_block_index)
        for s in self.spendable_list:
            f.write("%s\n" % s.as_text())
        f.close()
