from pycoin.ecdsa import generator_secp256k1, sign
import hashlib
import json
from ast import literal_eval  # 0.80 version required
import os
import sys

# Current directory: E:\Extra\Minhaz\Projects\Scalabale-blockchain-system\src\user_end
# Starting of this code, the location should be in src\user_end directory
# Otherwise the code will throw error or the structure of the folders will be disrupted
# tx_code_dir = os.getcwd()
# print(tx_code_dir)
# os.chdir("../..")
# src_dir = os.getcwd()
# sys.path.insert(1, src_dir)  # for importing folder_structure.py
# from folder_structure import output_tx


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
sender_address = "e94280055a972fa8a81ca3496a85c6e83237b6ec4c2c7f53e51fcdaee5f1fa37"
block_number = 1
receiver_address = "2b4e8a9e2d1f277d817b7d4df72c7897d5e9c4ce925eac0b7bbffcefa60e2e40"
sender_public_key = "0x4bfb2b4d18c8ff50a037b3b87fc4475f159f82cbc716fed126a84eb9f67d07c90x80fe121e34ab761266fad2b4db5b5c0283533364fff87fb127e9a899a1e52abc"
sender_private_key = ""
amount = 10
sender_info = [[sender_address, block_number]]
receiver_info = [{receiver_address: amount}]
tx_data = raw_tx_generator(sender_info, receiver_info, sender_public_key, sender_private_key)



# main()
