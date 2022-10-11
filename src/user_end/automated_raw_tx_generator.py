import json
import os
from pathlib import Path
import sys
a_tx_code_dir = os.getcwd()
# print(a_tx_code_dir)
os.chdir("..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import src_user_end
from key_pairs_address_generation import address_generation
from raw_tx_generator import main


# the code of sender_info is only for first tx
# for the second tx and the tx coming after that sender_info code will be changed, sender address will be the
# receiving address of the previous transaction
def initial_sender_info_generator():
    block_number = 1
    sender_address_file = json.loads(address_generation())
    sender_address = sender_address_file["address"]
    sender_public_key = sender_address_file["public_key"]
    sender_private_key = sender_address_file["private_key"]
    sender_info = [[sender_address, block_number]]
    # print("Sender info:", sender_info)
    return sender_info, sender_public_key, sender_private_key


def receiver_info_generator(receiver_address_lst_data, number_of_addresses, amount):
    receiver_info = []
    for r in range(number_of_addresses):
        receiver_address_file = json.loads(address_generation())
        receiver_address = receiver_address_file["address"]
        receiver_public_key = receiver_address_file["public_key"]
        receiver_private_key = receiver_address_file["private_key"]
        receiver_info.append({receiver_address: amount})
        receiver_address_lst_data.append(
            {"address": receiver_address, "public_key": receiver_public_key, "private_key": receiver_private_key})
    # print("Receiver info: ", receiver_info)
    return receiver_info, receiver_address_lst_data


def receiver_address_list(block_number, receiver_address_lst_data):
    name = "block_" + str(block_number) + "_receiver_addresses.txt"
    receiver_address_list_file_name = Path(src_user_end()) / name
    with open(receiver_address_list_file_name, 'w') as tx:
        json.dump(receiver_address_lst_data, tx, indent=2)
        # print('[receiver_address_lst updated]')
    # print("Receiver list data", receiver_address_lst_data)
    # print("length of Receiver list", len(receiver_address_lst_data))
    # print(receiver_address_list_file_name)


def initial_tx_generator():
    sender_info = initial_sender_info_generator()[0]
    sender_public_key = initial_sender_info_generator()[1]
    sender_private_key = initial_sender_info_generator()[2]
    receiver_address_lst_data = []
    i_receiver_info_generator_data = receiver_info_generator(receiver_address_lst_data, 2, 100000)
    receiver_info = i_receiver_info_generator_data[0]
    receiver_address_lst_data = i_receiver_info_generator_data[1]
    receiver_address_list(1, receiver_address_lst_data)
    main(sender_info, receiver_info, sender_public_key, sender_private_key)
    # print("initial receiver_address_list: ", receiver_address_lst_data)


def multiple_tx_generator(block_number, number_of_receiver_addresses_per_tx, amount):
    m_receiver_address_lst_data = []
    r_name = "block_" + str(block_number - 1) + "_receiver_addresses.txt"
    receiver_address_list_file_name = Path(src_user_end()) / r_name
    # print(f"{str(block_number - 1)} receiver_address_list_file_name: ", receiver_address_list_file_name)
    with open(receiver_address_list_file_name, 'r') as file:
        receiver_address_lst_data = json.loads(file.read())
    for each_receiver in receiver_address_lst_data:
        sender_address = each_receiver["address"]
        sender_public_key = each_receiver["public_key"]
        sender_private_key = each_receiver["private_key"]
        sender_info = [[sender_address, block_number]]
        receiver_info_generator_data = receiver_info_generator(m_receiver_address_lst_data, number_of_receiver_addresses_per_tx, amount)
        receiver_info = receiver_info_generator_data[0]
        m_receiver_address_lst_data = receiver_info_generator_data[1]
        main(sender_info, receiver_info, sender_public_key, sender_private_key)
    receiver_address_list(block_number, m_receiver_address_lst_data)
    # print("multiple receiver_address_list: ", m_receiver_address_lst_data)


# initial_tx_generator()
multiple_tx_generator(2, 4, 25000)
