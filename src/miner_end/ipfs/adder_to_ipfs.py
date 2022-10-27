import os
import json
import subprocess
import sys
from pathlib import Path
import time
ipfs_adder_code_dir = os.getcwd()
print(f"This codes directory: {ipfs_adder_code_dir}")
os.chdir("..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import output_tx, output_tx_cid, output_used_tx


def tx_adder(raw_tx_ab_file_name, cid_folder):
    with open(raw_tx_ab_file_name, "r") as file:
        content = file.read()
        unfrozen = json.loads(content)
    message = unfrozen["message"]
    receiver = message["ReceiverAddress"]
    rv_list = []
    for i in receiver:
        for k, v in i.items():
            rv_list.append(k)
    p = subprocess.check_output(f'ipfs add {raw_tx_ab_file_name}', shell=True, text=True)
    hash_ = p[6:52]
    num = hash_
    # C:\\Users\\Minhaz\\Desktop\\libp2p_show_room\\src\\Txn
    nume = str(num) + ".json"
    cid_file_name = os.path.join(cid_folder, nume)
    with open(cid_file_name, 'w') as loader:
        hash_file = {
            'CID': hash_, "ReceiverAddress": rv_list
        }
        var_ = json.dumps(hash_file, indent=2)
        loader.write(var_)


def delete_files(file_name, delete_file_dir, transafer_dir):
    ab_file_name_for_delete = Path(delete_file_dir) / file_name
    with open(ab_file_name_for_delete, "r") as file:
        content = json.loads(file.read())
    ab_file_name_for_transfer = Path(transafer_dir) / file_name
    with open(ab_file_name_for_transfer, "w") as file:
        data = json.dumps(content)
        file.write(data)
    os.remove(ab_file_name_for_delete)


def ipfs_add_main():
    tx_cid_dir = output_tx_cid()
    raw_tx_dir = output_tx()
    raw_tx_dir_lst = os.listdir(raw_tx_dir)
    for each_tx in raw_tx_dir_lst:
        raw_tx_file_name = each_tx
        raw_tx_ab_file_name = os.path.join(raw_tx_dir, raw_tx_file_name)
        tx_adder(raw_tx_ab_file_name= raw_tx_ab_file_name, cid_folder= tx_cid_dir)
        print(f"{raw_tx_file_name} is uploaded and cid is written")
        delete_files(file_name=each_tx, delete_file_dir=raw_tx_dir, transafer_dir=output_used_tx())
    print("All tx is uploaded to ipfs and cid is written")


ipfs_add_main()

