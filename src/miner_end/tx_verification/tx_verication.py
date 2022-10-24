import os
import json
import subprocess
import sys
from pycoin.ecdsa import generator_secp256k1, verify
import hashlib
from ast import literal_eval  # 0.80 version required
import subprocess
import time
from pathlib import Path

tx_verification_code_dir = os.getcwd()
print(f"tx verification code directory: {tx_verification_code_dir}")
os.chdir("../..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import ipfs_raw_tx_fetching, p2p_used_receiving_tx_cid
print("transaction verification code directory after folder structure: ", os.getcwd())


def sha3_256Hash(msg):
    hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")


def verifyECDSAsecp256k1(msg, signature, pubKey):
    msgHash = sha3_256Hash(msg)
    valid = verify(generator_secp256k1, pubKey, msgHash, signature)
    return valid


def signature_check(public_key_hex, signature_hex, message, count):
    # public key decoding
    p = public_key_hex[2:].find("x")
    public_key_hex_first = public_key_hex[:p + 1]
    public_key_hex_second = public_key_hex[p + 1:]
    public_key_first_int = literal_eval(public_key_hex_first)
    public_key_second_int = literal_eval(public_key_hex_second)
    public_key_tuple_int = (public_key_first_int, public_key_second_int)
    # signature decoding
    s = signature_hex[2:].find("x")
    signature_hex_first = signature_hex[:s + 1]
    signature_hex_second = signature_hex[s + 1:]
    signature_first_int = literal_eval(signature_hex_first)
    signature_second_int = literal_eval(signature_hex_second)
    signature_tuple_int = (signature_first_int, signature_second_int)

    msg = json.dumps(message)
    pubKey = public_key_tuple_int
    sig = signature_tuple_int
    if verifyECDSAsecp256k1(msg, sig, pubKey):
        print("passed signature test")
        count = count + 1
        print("count: ", count)
    else:
        print("Failed signature test")
    return count


def balance_check():
    pass


def double_spending_check():
    pass


def tx_verification_main():
    raw_tx_dir = ipfs_raw_tx_fetching()  # starting transaction verification process from this folder
    used_tx_cid_dir = p2p_used_receiving_tx_cid() # it folder will be used to send tx to mempool
    raw_tx_dir_lst = os.listdir(raw_tx_dir)
    for each_raw_tx in raw_tx_dir_lst:
        each_raw_tx_ab_dir = os.path.join(raw_tx_dir, each_raw_tx)
        with open(each_raw_tx_ab_dir, "r") as file:
            data_for_verification = json.loads(file.read())

        signature = data_for_verification["signature"]
        message = data_for_verification["message"]
        sender_address_lst = message["SenderAddress"]
        receiver_address_lst = message["ReceiverAddress"]
        public_key = message["PublicKey"]
        count = 0
        # verification starts
        sig_test = signature_check(public_key_hex=public_key, signature_hex=signature, message=message, count=count)
        print(f"{each_raw_tx} passed {sig_test} tests")

        # # writing mempool data starts
        # each_tx_cid_ab_dir = os.path.join(used_tx_cid_dir, each_raw_tx)
        # with open(each_tx_cid_ab_dir, "r") as file:
        #     data_for_mempool = json.loads(file.read())



