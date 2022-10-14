#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# MyOwnPeer2PeerNode is an example how to use the p2pnet.Node to implement your own peer-to-peer network node.        #
#######################################################################################################################
from p2pnetwork.node import Node
import json
import time
import random
import os


class MyOwnPeer2PeerNode(Node):
    counter = 0

    # Python class constructor
    def __init__(self, host, port):
        super(MyOwnPeer2PeerNode, self).__init__(host, port, None)
        print("MyPeer2PeerNode: Started")

    # all the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.

    def outbound_node_connected(self, node):
        print("outbound_node_connected: " + node.id)

    def inbound_node_connected(self, node):
        print("inbound_node_connected: " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: " + node.id)

    '''
    def node_message(self, node, data):
        data.update(time = time.time())
        with open("sample.json", "w") as outfile:
            json.dump(data, outfile) 

        print(time.time())
        #print(str(data))
    '''

    def node_message(self, node, data):

        # with open("sample" + str(random.randint(0,100)) + ".json", "w") as outfile:
        #    json.dump(data, outfile)

        # checking the received file is a block or transaction and save them in different directory--------------------
        key_list = list(data.keys())
        if "Index" not in key_list:
            print("It's a transaction")
            json_dir = "C:\\Users\\DELL\\Desktop\\Testing\\Test_1\\p2p_testing\\receiving_transaction_from_p2p"
            name = "sample_tx" + str(MyOwnPeer2PeerNode.counter) + ".json"
            t_fileName = os.path.join(json_dir, name)

            with open(t_fileName, "w") as outfile:
                json.dump(data, outfile)
                MyOwnPeer2PeerNode.counter = MyOwnPeer2PeerNode.counter + 1
        else:
            print("It's a block")
            block_dir = "C:\\Users\\DELL\\Desktop\\Testing\\Test_1\\p2p_testing\\receiving_block_from_p2p"
            # creating directory-------------------------------------
            try:
                os.makedirs(block_dir)
                print("Directory created successfully")
            except FileExistsError:
                print("Directory can not be created")
            # --------------------------------------------------------
            block_num = data["Index"]
            block_name = "sample_block" + str(block_num) + ".json"
            b_fileName = os.path.join(block_dir, block_name)

            with open(b_fileName, "w") as outfile:
                json.dump(data, outfile)
                MyOwnPeer2PeerNode.counter = MyOwnPeer2PeerNode.counter + 1
        # --------------------------------------------------------------------------------------------------------------

        print("Receiving Time: " + str(time.time()))

    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: " + node.id)

    def node_request_to_stop(self):
        print("node is requested to stop!")

