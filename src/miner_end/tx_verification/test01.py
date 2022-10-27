import time
import datetime
import os
import json
import sys
from pathlib import Path
from pycoin.ecdsa import generator_secp256k1, verify
import hashlib
from ast import literal_eval  # 0.80 version required
import subprocess

os.chdir("../..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import output_receiver_address_list, output_raw_block
print("transaction verification code directory after folder structure: ", os.getcwd())
present = time.time()
prs = time.ctime(present)
print("prs: ", type(prs))
print("present: ", present)
r_present = datetime.datetime.strptime(prs, "%a %b %d %H:%M:%S %Y")
return_present = r_present.timestamp()
print("return_present: ", return_present)

future = time.time()
ftr = time.ctime(future)
print("ftr: ", ftr)
print("future: ", future)


def receiver_list_update():
    r_list = []
    raw_block_dir = output_raw_block()
    block_name = Path(raw_block_dir) / "2.json"
    with open(block_name, "r") as file:
        block_data = json.loads(file.read())
    print(block_data)
    transactions = block_data["Transactions"]
    # print(transactions)
    for each_key in transactions.keys():
        print(each_key)
        for each_r in (transactions[each_key]["ReceiverAddress"]):
            r_list.append(each_r)
        # print(transactions[each_key]["ReceiverAddress"])

    # dif = int(ftr) - int(prs)
    receivers_dir = output_receiver_address_list()
    receivers_dir_lst = os.listdir(receivers_dir)
    receivers_name = os.path.join(receivers_dir, receivers_dir_lst[0])
    # with open(receivers_name, "r") as file:
    #     data = json.loads(file.read())
    #
    # print(r_list)
    # with open(receivers_name, "w") as file:
    #     file.write(json.dumps(r_list, indent=2))

    with open(receivers_name, "r") as file:
        data_2 = json.loads(file.read())
    print("Total Receiver Addresses: ", len(data_2))
