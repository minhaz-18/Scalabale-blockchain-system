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

node_1 = MyOwnPeer2PeerNode("192.168.31.234", 8001) ## My Laptop's Local IP ##
#node_2 = MyOwnPeer2PeerNode("0.0.0.0", 8080) 
#node_3 = MyOwnPeer2PeerNode("127.0.0.1", 8003) ## My Local Host ##

time.sleep(1)

node_1.start()
#node_2.start()
#node_3.start()

time.sleep(1)

#node_1.connect_with_node('103.149.142.66', 8001) ## Baten's PC ##
node_1.connect_with_node('45.249.103.97', 8080) ## My PC ##
node_1.connect_with_node('103.149.142.66', 8001) ## My PC ##
#node_1.connect_with_node('118.179.15.131', 8080) ## My PC ##

#node_1.connect_with_node('127.0.0.1', 8002)
#node_2.connect_with_node('127.0.0.1', 8003)
#node_3.connect_with_node('127.0.0.1', 8002)

#time.sleep(2)

print("Sending at: " + str(time.time()))
#node_1.send_to_nodes({"name": "Maurice", "number": 20})

'''
# For sending transaction ------------------------------------------------------------------------------
file_dir = "C:\\Users\\DELL\\Desktop\\Testing\\Test_1\\p2p_testing\\sending_transaction_to_p2p"
ls = os.listdir(file_dir )
#print(ls)
for file_num in ls:
    file_name = os.path.join(file_dir, file_num)
    with open(file_name) as file:
        data = json.load(file)
        node_1.send_to_nodes(data)
'''
# ------------------------------------------------------------------------------------------------------

'''
# For sending blocks -------------------------------------------------------------------------------------------------
block_file_dir = "C:\\Users\\DELL\\..........."  #this directory is only for sending files not the ultimate block directory
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
