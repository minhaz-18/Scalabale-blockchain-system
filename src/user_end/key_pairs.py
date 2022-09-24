from pycoin.ecdsa import generator_secp256k1
import secrets
import jsonpickle
import os
import time

st = time.time()


indexer = '00000000'

cwd = os.getcwd()

for i in range(0, 1):
    privKey = secrets.randbelow(generator_secp256k1.order())  # generated private key
    private_key_hex = hex(privKey)  # ultimate private key

    # public key generation
    pubKey = (generator_secp256k1 * privKey).pair()  # generated public key
    public_key_hex_tuple = (hex(pubKey[0]), hex(pubKey[1]))
    public_key_hex = hex(pubKey[0]) + hex(pubKey[1])  # ultimate public key


    # desired_folder = "C:\\Users\\DELL\\Desktop\\Testing\\Test_1\\generated_raw_transaction\\21000_(5)"
    desired_folder = "C:\\Users\\DELL\\Desktop\\Testing\\Test_1\\genesis_block"

    if "key_pairs" not in os.listdir(desired_folder):
        os.chdir(desired_folder)
        os.mkdir("key_pairs")
    # os.chdir("C:\\Users\\DELL\\Desktop\\Testing\\Test_1\\generated_raw_transaction\\21000_(5)\\key_pairs")
    os.chdir("C:\\Users\\DELL\\Desktop\\Testing\\Test_1\\genesis_block\\key_pairs")

    i_length = len(str(i + 1))
    # print(i_length)
    file_name = indexer[0:-i_length] + f"{i + 1}" + ".json"
    # print(file_number)

    keys_dict = {"public_key": public_key_hex, "private_key": private_key_hex}
    with open(file_name, "w") as file:
        frozen = jsonpickle.encode(keys_dict)
        file.write(frozen)
ft = time.time()
print("Starting time", st)
print("Finishing time ", ft)
print("Required time", ft-st)
print('[KEYS GENERATED]')