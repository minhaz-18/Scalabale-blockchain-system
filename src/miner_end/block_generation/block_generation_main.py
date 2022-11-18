import os
import sys
import time

block_generation_main_code_dir = os.getcwd()
print(f"block generation main code directory: {block_generation_main_code_dir}")
os.chdir("../..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import output_hash_block, output_raw_block, verified_tx_mempool, src_block_generation
src_block_generation_dir = src_block_generation()
sys.path.insert(1, src_block_generation_dir)
from raw_block_generation import raw_block_main
from block_ipfs_adder import block_ipfs_adder
from hash_block_generation import *


def block_generation_main(verified_tx_number):
    # raw block generation
    starting_time_for_raw_block = time.time()
    raw_block_main(verified_tx_number)
    finishing_time_for_raw_block = time.time()
    dif = finishing_time_for_raw_block - starting_time_for_raw_block
    print("starting time for raw block: ", time.ctime(starting_time_for_raw_block))
    print("finishing_time for raw block: ", time.ctime(finishing_time_for_raw_block))
    print("required time for raw block in sec: ", dif)
    print("required time for raw block: ", time.ctime(dif))

    # raw block add to ipfs
    block_ipfs_adder()

    # hash block generation
    starting_time_for_hash_block = time.time()
    hash_block_generation()
    finishing_time_for_hash_block = time.time()
    dif = finishing_time_for_hash_block - starting_time_for_hash_block
    print("starting time for hash block: ", time.ctime(starting_time_for_hash_block))
    print("finishing time for hash block: ", time.ctime(finishing_time_for_hash_block))
    print("required time for hash block in sec: ", dif)
    print("required time for hash block: ", time.ctime(dif))
    trasfer_mempool_data_after_hash_block_generation()


# block_generation_main(verified_tx_number=21000)