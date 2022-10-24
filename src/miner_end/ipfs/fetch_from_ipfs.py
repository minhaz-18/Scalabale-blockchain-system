import os
import json
import subprocess
import sys
from pathlib import Path
ipfs_fetcher_code_dir = os.getcwd()
print(f"ipfs fetch code directory: {ipfs_fetcher_code_dir}")
os.chdir("../..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import p2p_receiving_tx_cid, p2p_receiving_block_cid, ipfs_raw_tx_fetching, ipfs_raw_block_fetching, p2p_used_receiving_tx_cid, p2p_used_receiving_block_cid
print("ipfs directory after folder structure: ", os.getcwd())


def fetcher(x_cid_ab_file_name, raw_x_folder):
    with open(x_cid_ab_file_name, "r") as file:
        content = file.read()
        unfrozen = json.loads(content)
    # print("CID: ", unfrozen['CID'])
    p = subprocess.check_output(f"ipfs cat {unfrozen['CID']}", shell=True, text=True)
    raw_tx = json.loads(p)
    # print("Raw tx: ", raw_tx)
    nume = str(unfrozen['CID']) + ".json"
    raw_tx_file_name = os.path.join(raw_x_folder, nume)
    with open(raw_tx_file_name, 'w') as loader:
        var_ = json.dumps(raw_tx, indent=2)
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


def ipfs_tx_fetch_main():
    tx_cid_dir = p2p_receiving_tx_cid()
    used_tx_cid_dir = p2p_used_receiving_tx_cid()
    raw_tx_dir = ipfs_raw_tx_fetching()
    tx_cid_dir_lst = os.listdir(tx_cid_dir)
    for each_tx_cid in tx_cid_dir_lst:
        tx_cid_file_name = each_tx_cid
        tx_cid_ab_file_name = os.path.join(tx_cid_dir, tx_cid_file_name)
        fetcher(x_cid_ab_file_name=tx_cid_ab_file_name, raw_x_folder=raw_tx_dir)
        print(f"{tx_cid_ab_file_name} is fetched and raw_tx is written")
        delete_files(file_name=each_tx_cid, delete_file_dir=tx_cid_dir, transafer_dir=used_tx_cid_dir)
    print("All tx_cid is fetched from ipfs and raw_tx is written")


def ipfs_block_fetch_main():
    block_cid_dir = p2p_receiving_block_cid()
    used_block_cid_dir = p2p_used_receiving_block_cid()
    raw_block_dir = ipfs_raw_block_fetching()
    tx_cid_dir_lst = os.listdir(block_cid_dir)
    for each_block_cid in tx_cid_dir_lst:
        block_cid_file_name = each_block_cid
        print(each_block_cid)
        block_cid_ab_file_name = os.path.join(block_cid_dir, block_cid_file_name)
        fetcher(x_cid_ab_file_name=block_cid_ab_file_name, raw_x_folder=raw_block_dir)
        print(f"{block_cid_ab_file_name} is fetched and raw_tx is written")
        delete_files(file_name=each_block_cid, delete_file_dir=block_cid_dir, transafer_dir=used_block_cid_dir)
    print("All block_cid is fetched from ipfs and raw_block is written")


ipfs_tx_fetch_main()
# ipfs_block_fetch_main()

