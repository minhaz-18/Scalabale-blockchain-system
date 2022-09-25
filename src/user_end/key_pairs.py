from pycoin.ecdsa import generator_secp256k1
import secrets
import json
import os
import sys

code_dir = os.getcwd()
os.chdir("src")
src = os.getcwd()
sys.path.insert(1, src)  # for importing folder_structure.py
os.chdir(code_dir)  # returning to the code dir
from folder_structure import output_key_pairs


def key_pairs():
    privKey = secrets.randbelow(generator_secp256k1.order())  # generated private key
    private_key_hex = hex(privKey)  # ultimate private key

    # public key generation
    pubKey = (generator_secp256k1 * privKey).pair()  # generated public key
    public_key_hex_tuple = (hex(pubKey[0]), hex(pubKey[1]))
    public_key_hex = hex(pubKey[0]) + hex(pubKey[1])  # ultimate public key

    # key_pairs location
    key_folder_path = output_key_pairs()[0]
    key_folder_lst = output_key_pairs()[1]
    file_real_name = public_key_hex + ".json"
    file_name = os.path.join(key_folder_path, file_real_name)
    keys_dict = {"public_key": public_key_hex, "private_key": private_key_hex}
    with open(file_name, "w") as file:
        key_pairs = json.dumps(keys_dict, indent=4)
        file.write(key_pairs)
    # print('[KEYS GENERATED]')
    return key_pairs

# key_pairs()
