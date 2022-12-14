#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (MyOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the MyOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################
'''
node = this device's local ip and port number
node.connect = the connected device's public ip and port number
The ports should be port forwarded
firewall should be disabled or maybe not
sender's port number and receiver's port number's should match
'''

import sys
import time
import json
import os
# sys.path.insert(0, '..') # Import the files where the modules are located

from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
p2p_sending_code_dir = os.getcwd()
print(f"p2p sending code directory: {p2p_sending_code_dir}")
os.chdir("..")
src_dir = os.getcwd()
sys.path.insert(1, src_dir)  # for importing folder_structure.py
from folder_structure import p2p_sending_tx_cid, p2p_sending_block_cid, src_user_end, output_tx_cid, p2p_sending_block_cid
os.chdir(src_user_end())
print("p2p_sending_tx_cid: ", p2p_sending_tx_cid())
print("p2p_sending_block_cid: ", p2p_sending_block_cid())


def p2p(my_machine_loacl_ip, my_forwarded_port, connected_machine_1_public_ip, connected_machine_1_forwarded_port, connected_machine_2_public_ip, connected_machine_2_forwarded_port):
    node_1 = MyOwnPeer2PeerNode(my_machine_loacl_ip, my_forwarded_port) ## Minhaz's Pc Local IP ##
    time.sleep(1)
    node_1.start()
    time.sleep(1)
    node_1.connect_with_node(connected_machine_1_public_ip, connected_machine_1_forwarded_port) ## Minhaz's laptop Public ip ##
    node_1.connect_with_node(connected_machine_2_public_ip, connected_machine_2_forwarded_port) ## Minhaz's laptop Public ip ##
    print("Sending at: " + str(time.time()))
    #node_1.send_to_nodes({"name": "Maurice", "number": 20})


    # while True:
    # For sending blocks -------------------------------------------------------------------------------------------------
    block_file_dir = p2p_sending_block_cid()  # this directory is only for sending files not the ultimate block directory
    block_ls = os.listdir(block_file_dir)
    if len(block_ls) != 0:
        for each_block in block_ls:
            block_file_name = os.path.join(block_file_dir, each_block)
            with open(block_file_name) as file:
                data = json.load(file)
                node_1.send_to_nodes(data)
        for each_block_for_del in block_ls:
            block_name_for_del = os.path.join(block_file_dir, each_block_for_del)
            os.remove(block_name_for_del)
        print("All blocks are deleted")
    # --------------------------------------------------------------------------------------------------------------------
    # For sending transaction ------------------------------------------------------------------------------
    tx_file_dir = output_tx_cid()
    tx_ls = os.listdir(tx_file_dir)
    if len(tx_ls) != 0:
        #print(ls)
        for file_num in tx_ls:
            file_name = os.path.join(tx_file_dir, file_num)
            with open(file_name) as file:
                data = json.load(file)
                node_1.send_to_nodes(data)
        for file_num_for_del in tx_ls:
            file_name_for_del = os.path.join(tx_file_dir, file_num_for_del)
            os.remove(file_name_for_del)
        print("All transactions are deleted")

    # ------------------------------------------------------------------------------------------------------
    #time.sleep(5)
    #node_1.stop()
    #node_2.stop()
    #node_3.stop()
    print('end test')


# my_machine_loacl_ip = "192.168.0.106"
# my_forwarded_port = 8083
#
# connected_machine_1_public_ip = "144.48.162.18"
# connected_machine_1_forwarded_port = 8081
# connected_machine_2_public_ip = "144.48.162.18"
# connected_machine_2_forwarded_port = 8082


# p2p(my_machine_loacl_ip, my_forwarded_port, connected_machine_1_public_ip, connected_machine_1_forwarded_port, connected_machine_2_public_ip, connected_machine_2_forwarded_port)