import subprocess
import os
import json
import time
import sys

block_ipfs_adder_code_dir = os.getcwd()
print(f"block ipfs adder code directory: {block_ipfs_adder_code_dir}")
os.chdir("../..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import output_raw_block, output_raw_block_cid
os.chdir(block_ipfs_adder_code_dir)


def block_ipfs_adder():
    raw_block_dir = output_raw_block()
    raw_block_cid_dir = output_raw_block_cid()
    raw_block_dir_lst = os.listdir(raw_block_dir)
    new = []
    for i in raw_block_dir_lst:
        num = i.split(".json")
        print(num[0])
        new.append(int(num[0]))
    new.sort()
    last_file_name = str(new[-1]) + ".json"
    last_raw_block_name = os.path.join(raw_block_dir, last_file_name)
    with open(last_raw_block_name, 'r') as file:
        content = file.read()
        unfrozen = json.loads(content)
    number = unfrozen["Index"]
    num = str(number)
    p = subprocess.check_output(f'ipfs add {last_raw_block_name}', shell=True, text=True)
    hash_ = p[6:52]

    raw_block_cid_name = num + ".json"
    raw_block_cid_ab_name = os.path.join(raw_block_cid_dir, raw_block_cid_name)
    with open(raw_block_cid_ab_name, 'w') as loader:
        hash_file = {
            'Index': number, 'CID': hash_, "Timestamp": time.time()
        }
        var_ = json.dumps(hash_file, indent=2)
        loader.write(var_)
    print(hash_)

