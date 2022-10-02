from pycoin.ecdsa import generator_secp256k1
# from pycoin.ecdsa.secp256k1 import secp256k1_generator
import secrets
import json
import os
import sys
import time
import hashlib

<<<<<<< HEAD
code_dir = os.getcwdb()
os.chdir("E:\BlockChain\Scalabale-blockchain-system\src")
src = os.getcwd()
sys.path.insert(1, src)  # for importing folder_structure.py
os.chdir(code_dir)  # returning to the code dir
=======
code_dir = os.getcwd()
print(code_dir)
# os.chdir("..")
# os.chdir("src")
# src = os.getcwd()
sys.path.insert(1, code_dir)  # for importing folder_structure.py
# os.chdir(code_dir)  # returning to the code dir
>>>>>>> a2887fd832debb2a7870c4f6420e276b86a9cd5a
from folder_structure import output_key_pairs, output_addresses


def key_pairs_generation():
<<<<<<< HEAD
    privKey = secrets.randbelow(secp256k1_generator.order())  # generated private key
    private_key_hex = hex(privKey)  # ultimate private key

    # public key generation
    pubKey = (secp256k1_generator * privKey).pair()  # generated public key
=======
    # privKey = secrets.randbelow(generator_secp256k1.order())  # generated private key
    privKey = secrets.randbelow(generator_secp256k1.order())  # generated private key
    
    private_key_hex = hex(privKey)  # ultimate private key

    # public key generation
    # pubKey = (generator_secp256k1 * privKey).pair()  # generated public key
    pubKey = (generator_secp256k1 * privKey).pair()  # generated public key
>>>>>>> a2887fd832debb2a7870c4f6420e276b86a9cd5a
    public_key_hex_tuple = (hex(pubKey[0]), hex(pubKey[1]))
    public_key_hex = hex(pubKey[0]) + hex(pubKey[1])  # ultimate public key
    keys_dict = {"public_key": public_key_hex, "private_key": private_key_hex}

    # json_formatted_key_dict = json.dumps(keys_dict, indent=4)

    return keys_dict


def address_generation():
    publickey = key_pairs_generation()["public_key"]
    # creating the address block with public key and timestamp
    timestamp = time.time()
    block = {"public_key": publickey, "Timestamp": timestamp}
    json_format = json.dumps(block, sort_keys=True).encode()
    address = hashlib.sha256(json_format).hexdigest()

    address_block = {"address": address, "public_key": publickey, "timestamp": timestamp}
    # json_formatted_address_block = json.dumps(address_block, indent=4)
    return address_block


def write_files(folder_path, file_real_name, data):
    file_name = os.path.join(folder_path, file_real_name)
    with open(file_name, "w") as file:
        json_formatted = json.dumps(data, indent=4)
        file.write(json_formatted)


def main_file():
    # writing key_pairs
    # key_pairs location
    key_folder_path = output_key_pairs()[0]
    # key_folder_lst = output_key_pairs()[1]
    key_data = key_pairs_generation()
    public_key = key_data["public_key"]
    key_pairs_file_name = public_key + ".json"
    write_files(key_folder_path, key_pairs_file_name, key_data)
    
    # writing address
    # key_pairs location
    address_folder_path = output_addresses()[0]
    # key_folder_lst = output_key_pairs()[1]
    address_data = address_generation()
    # address = address_data["public_key"]
    address_file_name = public_key + ".json"
    write_files(address_folder_path, address_file_name, address_data)


main_file()

