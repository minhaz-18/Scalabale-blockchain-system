import time
import hashlib
import json
import os
import sys

raw_block_generation_code_dir = os.getcwd()
print(f"raw block generation code directory: {raw_block_generation_code_dir}")
os.chdir("../..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import output_hash_block, output_raw_block, verified_tx_mempool
os.chdir(raw_block_generation_code_dir)


def raw_block(data):
    # PREVIOUS BLOCK NUMBER AND PREVIOUS HASH NUMBER EXTRACT
    hash_block_dir = output_hash_block()
    hash_block_dir_lst = os.listdir(hash_block_dir)
    # print(hash_block_dir_lst)
    if len(hash_block_dir_lst) != 0:
        hash_block_dir_lst.sort()
        last_hash_block_name = os.path.join(hash_block_dir, hash_block_dir_lst[-1])

        # read the last file from the ultimate_block folder and get previous hash
        with open(last_hash_block_name, 'r') as file:
            content = file.read()
            hash_block_info = json.loads(content)
        previous_hash = hash_block_info["Block Hash"]
        last_hash_block_index = hash_block_info["Index"]
        index = last_hash_block_index + 1
    else:
        previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
        last_hash_block_index = 0
        index = last_hash_block_index + 1
    # RAW BLOCK FORMAT
    timestamp = int(time.time())
    print("timestamp: ", timestamp)
    nonce = 0
    block = {"Index": index,
             "Nonce": nonce,
             "Timestamp": timestamp,
             "Previous Hash": previous_hash,
             "Transactions": data
             }
    # GENERATE RAW BLOCK
    json_format = json.dumps(block, sort_keys=True).encode()   # json format
    hash_of_block = hashlib.sha256(json_format).hexdigest()    # generating hash
    print("Initial calculated hash: ", hash_of_block)
    while hash_of_block[:4] != "0000":        # checking is the block valid or not
        nonce += 1
        timestamp = int(time.time())
        block = {"Index": index,
                 "Nonce": nonce,
                 "Timestamp": timestamp,
                 "Previous Hash": previous_hash,
                 "Transactions": data
                 }       # incrementing nonce for validation purpose
        json_format = json.dumps(block, sort_keys=True).encode()  # again creating json format after updating block nonce
        hash_of_block = hashlib.sha256(json_format).hexdigest()  # again generating hash with updated block
        print("Calculated hash: ", hash_of_block)
    a = {"Block Hash": hash_of_block}
    block.update(a)
    print(block)

    # RAW BLOCK WRITE
    raw_block_number = str(index)
    raw_block_name = raw_block_number +".json"
    raw_block_dir = output_raw_block()
    file_name = os.path.join(raw_block_dir, raw_block_name)
    with open(file_name, "w") as file:
        gen = json.dumps(block, indent=2)
        file.write(gen)
    print(f"{raw_block_name} raw block is created and written in '{raw_block_dir_2}'")


def raw_block_main(num):
    mempool_dir = verified_tx_mempool()
    mempool_dir_lst = os.listdir(mempool_dir)
    if len(mempool_dir_lst) == num:
        print("Required numbered of transaction/ transactions are found in mempool")
        # EXTRACT TX DATA
        data = {}
        for i in mempool_dir_lst:
            tx_file_name = i
            file_index = mempool_dir_lst.index(i)
            file_name = os.path.join(mempool_dir, tx_file_name)

            with open(file_name, "r") as file:
                content = file.read()
                tx_info = json.loads(content)
            number = file_index + 1
            num = str(number)
            new_dict = {number: tx_info}
            data.update(new_dict)
        tx = data
        raw_block(tx)
