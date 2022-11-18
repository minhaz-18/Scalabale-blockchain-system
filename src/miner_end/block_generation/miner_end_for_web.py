import os
import sys
import json
import subprocess
import time
miner_end_for_web_code_dir = os.getcwd()
print(f"miner_end_for_web_code_dir: {miner_end_for_web_code_dir}")
os.chdir("../..")
src_dir = os.getcwd()

sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import output_raw_block, output_raw_block_cid, output_hash_block, verified_tx_mempool
os.chdir(miner_end_for_web_code_dir)


def before_mining():
    hash_block_dir = output_hash_block()
    mempool_dir = verified_tx_mempool()

    hash_block_list = os.listdir(hash_block_dir)
    total_block_number = len(hash_block_list)
    validated_tx_list = os.listdir(mempool_dir)
    total_validated_tx = len(validated_tx_list)
    hash_block_paths = [os.path.join(hash_block_dir, basename) for basename in hash_block_list]
    last_block_name = max(hash_block_paths, key=os.path.getctime)
    print(last_block_name)
    with open(last_block_name, "r") as file:
        content = json.loads(file.read())
    block_cid = content["CID"]
    p = subprocess.check_output(f"ipfs cat {block_cid}", shell=True, text=True)
    last_block_info = json.loads(p)
    return total_block_number, total_validated_tx, last_block_info

# var_before_mining = before_mining()
# total_block_number_before_mining = var_before_mining[0]
# total_validated_tx_before_mining = var_before_mining[1]
# last_block_info_before_mining = var_before_mining[2]


def after_mining():
    hash_block_dir = output_hash_block()
    mempool_dir = verified_tx_mempool()

    hash_block_list = os.listdir(hash_block_dir)
    total_block_number = len(hash_block_list)
    validated_tx_list = os.listdir(mempool_dir)
    total_validated_tx = len(validated_tx_list)
    hash_block_paths = [os.path.join(hash_block_dir, basename) for basename in hash_block_list]
    last_block_name = max(hash_block_paths, key=os.path.getctime)
    print(last_block_name)
    with open(last_block_name, "r") as file:
        content = json.loads(file.read())
    block_cid = content["CID"]
    p = subprocess.check_output(f"ipfs cat {block_cid}", shell=True, text=True)
    last_block_info = json.loads(p)
    return total_block_number, total_validated_tx, last_block_info


# var_after_mining = after_mining()
# total_block_number_after_mining = var_after_mining[0]
# total_validated_tx_after_mining = var_after_mining[1]
# last_block_info_after_mining = var_after_mining[2]
