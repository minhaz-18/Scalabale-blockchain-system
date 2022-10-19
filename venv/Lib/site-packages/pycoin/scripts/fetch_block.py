#!/usr/bin/env python

import sys

from pycoin.serialize import h2b_rev
from pycoin.serialize.bitcoin_streamer import stream_struct
from pycoin.services.insight import InsightService

URL = "https://search.bitaccess.ca/"

def main():
    SERVICE = InsightService(URL)
    import pdb; pdb.set_trace()
    block_hash = h2b_rev(sys.argv[1])
    out_bin = sys.argv[2]
    bh, t_hashes = SERVICE.get_blockheader_with_transaction_hashes(block_hash)
    txs = [SERVICE.get_tx(th) for th in t_hashes]
    f = open(out_bin, "wb")
    bh.stream(f)
    stream_struct("I", f, len(txs))
    for t in txs:
        t.stream(f)
    f.close()

if __name__ == '__main__':
    main()