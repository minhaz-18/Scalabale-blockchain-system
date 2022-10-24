#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (MyOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the MyOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################

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
from folder_structure import p2p_sending_tx_cid, p2p_sending_block_cid, src_user_end
os.chdir(src_user_end())
print("p2p_sending_tx_cid: ", p2p_sending_tx_cid())
print("p2p_sending_block_cid: ", p2p_sending_block_cid())

node_1 = MyOwnPeer2PeerNode("192.168.0.217", 8001) ## Minhaz's Local IP ##
# node_1 = MyOwnPeer2PeerNode("192.168.0.105", 8001) ## Opu's Local IP ##
# node_1 = MyOwnPeer2PeerNode("144.48.162.18", 8001) ## Minhaz's pubic IP ##
# node_1 = MyOwnPeer2PeerNode("202.65.175.47", 8001) ## Opu's pubic IP ##
#node_2 = MyOwnPeer2PeerNode("0.0.0.0", 8080)
#node_3 = MyOwnPeer2PeerNode("127.0.0.1", 8003) ## My Local Host ##

time.sleep(1)

node_1.start()
#node_2.start()
#node_3.start()

time.sleep(1)

# node_1.connect_with_node('104.28.208.86', 8080) ## Sohan's public PC ##
# node_1.connect_with_node('192.168.0.102', 8080) ## Sohan's local PC ##
# node_1.connect_with_node('192.168.0.105', 8001) ## Opu's Local PC ##
# node_1.connect_with_node('192.168.0.217', 8001) ## Minhaz's Local PC ##
node_1.connect_with_node('202.65.175.47', 8080) ## Opu's Public PC ##
#node_1.connect_with_node('144.48.162.18', 8080) ## Minhaz's Public PC ##

#node_1.connect_with_node('127.0.0.1', 8002)
#node_2.connect_with_node('127.0.0.1', 8003)
#node_3.connect_with_node('127.0.0.1', 8002)

#time.sleep(2)

print("Sending at: " + str(time.time()))
#node_1.send_to_nodes({"name": "Maurice", "number": 20})


# For sending transaction ------------------------------------------------------------------------------
tx_file_dir = p2p_sending_tx_cid()
ls = os.listdir(tx_file_dir)
#print(ls)
for file_num in ls:
    file_name = os.path.join(tx_file_dir, file_num)
    with open(file_name) as file:
        data = json.load(file)
        node_1.send_to_nodes(data)
        # os.remove(file_name)

# ------------------------------------------------------------------------------------------------------

'''
# For sending blocks -------------------------------------------------------------------------------------------------
block_file_dir = p2p_sending_block_cid()  #this directory is only for sending files not the ultimate block directory
block_ls = os.listdir(block_file_dir)
while True:
    if len(block_ls) != 0:
        block_file_name = os.path.join(block_file_dir, block_ls[0])
        with open(block_file_name) as file:
            data = json.load(file)
            node_1.send_to_nodes(data)
            os.remove(block_file_name)
# --------------------------------------------------------------------------------------------------------------------

'''


#time.sleep(5)

#node_1.stop()
#node_2.stop()
#node_3.stop()
print('end test')
