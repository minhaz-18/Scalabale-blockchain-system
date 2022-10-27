from pycoin.ecdsa import generator_secp256k1, sign
import hashlib
import json
from ast import literal_eval  # 0.80 version required
import os
import sys

# Current directory: E:\Extra\Minhaz\Projects\Scalabale-blockchain-system\src\user_end
# Starting of this code, the location should be in src\user_end directory
# Otherwise the code will throw error or the structure of the folders will be disrupted
tx_code_dir = os.getcwd()
print(tx_code_dir)
os.chdir("..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import output_tx


def sha3_256Hash(msg):
    hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")


def signECDSAsecp256k1(msg, privKey):
    msgHash = sha3_256Hash(msg)
    signature = sign(generator_secp256k1, privKey, msgHash)
    return signature


def message_generator(sender_info, receiver_info, public_key):
    message = {"SenderAddress": sender_info,
               "ReceiverAddress": receiver_info,
               "PublicKey": public_key
               }
    return message


def signature_output(message, sender_private_key):
    private_key_int = literal_eval(sender_private_key)
    privKey = private_key_int
    msg = json.dumps(message)
    signature = signECDSAsecp256k1(msg, privKey)
    signature_tuple_hex = (hex(signature[0]), hex(signature[1]))
    signature_hex = hex(signature[0]) + hex(signature[1])  # ultimate signature
    return signature_hex


# format
# sender_info = [[sender_address, block_number]]
# receiver_info = [{receiver_address: amount}]
def raw_tx_generator(sender_info, receiver_info, sender_public_key, sender_private_key):
    message = message_generator(sender_info, receiver_info, sender_public_key)
    print(message)

    signature_hex = signature_output(message, sender_private_key)
    print(signature_hex)

    user_tx = {
        'message': message,
        'signature': signature_hex
    }
    return user_tx


def write_tx(user_tx):
    tx_file_dir = output_tx()
    # print(f"tx file directory: {tx_file_dir}")
    total_file_number = len(os.listdir(tx_file_dir))
    print(total_file_number)
    tx_file_name = str(total_file_number+1) + ".json"
    tx_ab_file_name = os.path.join(tx_file_dir, tx_file_name)
    with open(tx_ab_file_name, 'w') as tx:
        json.dump(user_tx, tx, indent=2)
        print('[TRANSACTION WRITTEN]')


# # format
# receiverd_list = {"sender_address": "aksldj", "sadl": 12}
# sender_address = receiverd_list["sender_address"]
# sender_info = [[sender_address, block_number]]
# receiver_info = [{receiver_address: amount}]
def main(sender_info, receiver_info, sender_public_key, sender_private_key):
    # sender_address = "7195c17a19d70ce2e4ef28aac7016e60d30c948017d1261bd87bef48c6643465"
    # block_number = 3
    # receiver_address = "7195c17a19d70ce2e4ef28aac7016e60d30c948017d1261bd87bef48c6643465"
    # amount = 100
    # sender_public_key = "0x5d04a72eba03cec2b2fde3c2d98165b7f591853a6d9af6f719a84070765d32110x2766076891b3844707dbd99da97612954aff5158ad94cfd817d929e4f1b1c065 "
    # sender_private_key = "0xaccdb63dc692e835805470e998063be80acf15ab0d41b78acaf437ef64c9db74"
    # sender_info = [[sender_address, block_number]]
    # receiver_info = [{receiver_address: amount}]
    tx_data = raw_tx_generator(sender_info, receiver_info, sender_public_key, sender_private_key)
    write_tx(tx_data)
    return tx_data


# main()
