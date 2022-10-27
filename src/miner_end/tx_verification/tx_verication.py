import os
import json
import sys
from pycoin.ecdsa import generator_secp256k1, verify
import hashlib
from ast import literal_eval  # 0.80 version required
import subprocess

tx_verification_code_dir = os.getcwd()
print(f"tx verification code directory: {tx_verification_code_dir}")
os.chdir("../..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import ipfs_raw_tx_fetching, p2p_used_receiving_tx_cid, verified_tx_mempool, verified_tx_used_raw_tx_fetched_from_ipfs, output_hash_block, output_receiver_address_list
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


def balance_check(count, sender_address_lst, receiver_address_lst):
    hash_block_dir = output_hash_block()
    hash_block_dir_lst = os.listdir(hash_block_dir)
    if len(hash_block_dir_lst) == 0:
        print("No block is generated yet")
        print("Passed balance check")
        count = count + 1
    else:
        print("Some block has generated")
        # block number check -----------------------------------------------------------------
        all_sender_amount = 0
        # print(sender_address_lst)
        for s in sender_address_lst:
            block_no = s[-1]
            # print(block_no)
            sender_address = s[0]
            # print(sender_address)
            # read the block with this block_number from block directory
            number = str(block_no)
            hash_block_dir = output_hash_block()
            u_b_num = number + ".json"
            ultimate_block_name = os.path.join(hash_block_dir, u_b_num)
            with open(ultimate_block_name, "r") as file:
                content = file.read()
                unfrozen = json.loads(content)
            block_cid = unfrozen["CID"]
            # print(f"BLOCK CID : {block_cid}")
            # GO to IPFS and get the block information
            p = subprocess.check_output(f"ipfs cat {block_cid}", shell=True, text=True)
            block_info = json.loads(p)
            tx = block_info["Transactions"]
            # print(f"TRANSACTION: {tx}")
            # collect the corresponding CID of a certain received address
            for i in tx.keys():
                b = tx[i]
                r_v = b["ReceiverAddress"]
                # print(r_v)
                cid = b["CID"]
                # print(cid)
                for r_v_from_raw_block in r_v:
                    if r_v_from_raw_block == sender_address:  # ############################ check ###################################
                        # print(cid)
                        # GO to IPFS and get the information
                        t = subprocess.check_output(f"ipfs cat {cid}", shell=True, text=True)
                        tx_info = json.loads(t)
                        # check tx's sender address = information's receiver address
                        tx_info_message = tx_info["message"]
                        tx_info_receiver = tx_info_message["ReceiverAddress"]
                        # print(tx_info_receiver)
                        for each_item in tx_info_receiver:
                            for r in each_item.keys():
                                # print(r)
                                if r == sender_address:
                                    one_sender_address_amount = each_item[r]
                                    all_sender_amount = all_sender_amount + one_sender_address_amount
        receiver_total_amount = 0
        for r_a in receiver_address_lst:
            for k, v in r_a.items():
                receiver_total_amount = receiver_total_amount + float(v)
        # print(f"ALL SENDER AMOUNT : {all_sender_amount}")
        # print(f"ALL RECEIVER AMOUNT : {receiver_total_amount}")

        # check tx's amount => information's amount
        if all_sender_amount >= receiver_total_amount:
            print("Passed balance check")
            count = count + 1
            print("Count: ", count)
        else:
            print("Failed balance check")
    return count


def double_spending_check(count, sender_address_lst):
    receiver_address_list_dir = output_receiver_address_list()
    receiver_address_list_text_name = os.path.join(receiver_address_list_dir, "unused_addresses.txt")
    with open(receiver_address_list_text_name, "r") as file:
        content = file.read()
        unfrozen = json.loads(content)
    receiver_list = unfrozen
    # print("receiver_list first: ", receiver_list)
    length_of_receiver_list = len(receiver_list)
    if length_of_receiver_list == 0:
        print("Receiver list is empty")
        print("passed double spending test")
        count = count + 1
        print("Count: ", count)
    else:
        # reading receiver list file
        verified_sender_list = []
        # print(sender_address_lst)
        for s_a in sender_address_lst:
            # print(s_a)
            # for s_a in each_sender:
            # print(s_a)
            sender_address = s_a[0]
            # print(sender_address)
            receiver_address_list_text_name = os.path.join(receiver_address_list_dir, "unused_addresses.txt")
            with open(receiver_address_list_text_name, "r") as file:
                content = file.read()
                unfrozen = json.loads(content)
            receiver_list = unfrozen

            # checking sender address from fetch file is in receiver list file
            if sender_address in receiver_list:
                verified_sender_list.append(sender_address)
                # if matches then the transaction is valid and remove the address from receiver list file
                receiver_list.remove(sender_address)
                # for multiple sender receiver list must be updated multiple time
                # update receiver list
                with open(receiver_address_list_text_name, "w") as file:
                    frozen = json.dumps(receiver_list, indent=2)
                    file.write(frozen)
            # ------------------------------------------------------------------------------------------------------------
            # all the receiver address will be updated at a time in the list after verifying the whole tx
        actual_sender_list = []
        for a_s_l in sender_address_lst:
            # print(f"a_s_l : {a_s_l}")
            # for a_s_l in a_s_l_each_item:
            actual_sender_list.append(a_s_l[0])
        if verified_sender_list == actual_sender_list:
            print("passed double spending test")
            count = count + 1
            print("Count: ", count)
        else:
            print("Failed double spending test")
    return count


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
        balance_test = balance_check(count=sig_test, sender_address_lst=sender_address_lst, receiver_address_lst=receiver_address_lst)
        print(f"{each_raw_tx} passed {balance_test} tests")
        double_spending_test = double_spending_check(count=balance_test, sender_address_lst=sender_address_lst)
        print(f"{each_raw_tx} passed {double_spending_test} tests")
        if double_spending_test == 3:
            print(f"The {each_raw_tx} has passed all tests")
            # receiver addresses add to the unused_address_list
            # print("RECEIVER_ADDRESS_LIST : ", receiver_address_lst)
            for a_r_l_each_item in receiver_address_lst:
                # print("a_r_l_each_item: ", a_r_l_each_item)
                for a_r_l, amount in a_r_l_each_item.items():
                    receiver_address = a_r_l
                    # print("receiver_address: ", receiver_address)
                    receiver_address_list_dir = output_receiver_address_list()
                    receiver_address_list_text_name = os.path.join(receiver_address_list_dir, "unused_addresses.txt")
                    with open(receiver_address_list_text_name, "r") as file:
                        content = file.read()
                        unfrozen = json.loads(content)
                    unfrozen.append(receiver_address)
                    # print("unfrozen: ", unfrozen)
                    with open(receiver_address_list_text_name, "w") as file:
                        frozen = json.dumps(unfrozen)
                        file.write(frozen)

            # WRITING MEMOOL DATA
            each_tx_cid_ab_dir = os.path.join(used_tx_cid_dir, each_raw_tx)
            with open(each_tx_cid_ab_dir, "r") as file:
                data_for_mempool = json.loads(file.read())
            mempool_dir = verified_tx_mempool()
            each_tx_cid_ab_dir_for_mempool = os.path.join(mempool_dir, each_raw_tx)
            with open(each_tx_cid_ab_dir_for_mempool, "w") as file:
                file.write(json.dumps(data_for_mempool, indent=2))
            print(f"{each_raw_tx} is verified and writen in mempool")

            # REMOVE FROM P2P/USED_RECEIVING_TX_CID AND ADDING TO verified_tx/used_raw_tx_fetched_from_ipfs
            used_verified_raw_tx_dir = verified_tx_used_raw_tx_fetched_from_ipfs()
            each_raw_tx_ab_dir_for_delete = os.path.join(used_verified_raw_tx_dir, each_raw_tx)
            with open(each_raw_tx_ab_dir_for_delete, "w") as file:
                file.write(json.dumps(data_for_verification, indent=2))
            print(f"{each_raw_tx} is added in verified_tx/used_raw_tx_fetched_from_ipfs")

        else:
            print(f"The {each_raw_tx} has passed {double_spending_test} tests and is REJECTED")

        # REMOVE FROM P2P/USED_RECEIVING_TX_CID
        os.remove(each_raw_tx_ab_dir)
        print(f"{each_raw_tx} is deleted from ipfs/raw_tx_fetching")
        each_tx_cid_ab_dir = os.path.join(used_tx_cid_dir, each_raw_tx)
        os.remove(each_tx_cid_ab_dir)
        print(f"{each_raw_tx} is deleted from p2p/used_receiving_tx_cid")



tx_verification_main()



