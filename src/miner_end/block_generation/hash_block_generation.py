import time
import hashlib
import json
import os
import sys
hash_block_generation_code_dir = os.getcwd()
print(f"hash block generation code directory: {hash_block_generation_code_dir}")
os.chdir("../..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import output_hash_block, output_raw_block_cid, p2p_sending_block_cid
print("hash block generation code directory after folder structure: ", os.getcwd())


def hash_block_generation():
    raw_block_cid_dir = output_raw_block_cid()
    raw_block_cid_dir_lst = os.listdir(raw_block_cid_dir)
    raw_block_cid_paths = [os.path.join(raw_block_cid_dir, basename) for basename in raw_block_cid_dir_lst]
    last_raw_block_cid_name = max(raw_block_cid_paths, key=os.path.getctime)

    # read the last file from the block_cid_generation folder and get index, cid
    with open(last_raw_block_cid_name, 'r') as file:
        content = file.read()
        unfrozen = json.loads(content)
    number = unfrozen["Index"]
    cid = unfrozen["CID"]
    h_index = number
    data = cid

    hash_block_dir = output_hash_block()
    hash_block_dir_lst = os.listdir(hash_block_dir)
    if len(hash_block_dir_lst) != 0:
        # determine the last file in the ultimate_block folder
        u_path = hash_block_dir
        files = os.listdir(u_path)
        hash_block_paths = [os.path.join(u_path, basename) for basename in files]
        last_block_name = max(hash_block_paths, key=os.path.getctime)

        # read the last file from the ultimate_block folder and get previous hash
        with open(last_block_name, 'r') as file:
            content = file.read()
            ultimate_block_info = json.loads(content)
        previous_hash = ultimate_block_info["Block Hash"]
    else:
        previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    timestamp = time.time()
    nonce = 0
    block = {"Index": h_index,
             "Nonce": nonce,
             "Timestamp": timestamp,
             "Previous Hash": previous_hash,
             "CID": data
             }

    json_format = json.dumps(block, sort_keys=True).encode()   # json format
    hash_of_block = hashlib.sha256(json_format).hexdigest()    # generating hash
    while hash_of_block[:2] != "00":        # checking if the block valid or not
        nonce += 1
        timestamp = time.time()
        block = {"Index": h_index,
                 "Nonce": nonce,
                 "Timestamp": timestamp,
                 "Previous Hash": previous_hash,
                 "CID": data
                 }       # incrementing nonce for validation purpose
        json_format = json.dumps(block, sort_keys=True).encode()  # again creating json format after updating block nonce
        hash_of_block = hashlib.sha256(json_format).hexdigest()  # again generating hash with updated block
    a = {"Block Hash": hash_of_block}
    block.update(a)

    # WRITE THE HASH BLOCK IN HASH BLOCK FOLDER
    hash_block_name = str(h_index) + ".json"
    hash_block_ab_name = os.path.join(hash_block_dir, hash_block_name)
    with open(hash_block_ab_name, "w") as file:
        block_data = json.dumps(block, indent=2)
        file.write(block_data)
    print(f"{hash_block_name} number hash block is written in '{hash_block_dir}'")
    # WRITE THE HASH BLOCK IN P2P SENDEING BLOCK FOLDER
    p2p_sending_hash_block_dir = p2p_sending_block_cid()
    hash_block_for_p2p_ab_name = os.path.join(p2p_sending_hash_block_dir, hash_block_name)
    with open(hash_block_for_p2p_ab_name, "w") as file:
        block_data = json.dumps(block, indent=2)
        file.write(block_data)
    print(f"{hash_block_name} number hash block is written in '{p2p_sending_hash_block_dir}'")
    return block


hash_block_generation()
