import os

dir = os.getcwd()
print(dir)
os.chdir("src")
src_dir = os.getcwd()
print(src_dir)


# project
def project():
    os.chdir(src_dir)
    os.chdir("..")
    project_dir = os.getcwd()
    project_lst = os.listdir(project_dir)
    return project_dir, project_lst


def create_folder(name, lst):
    if name not in lst:
        # print(f"{name} does not exists yet")
        os.mkdir(name)
        # print(f"{name} has been created")
        os.chdir(name)
        folder_dir = os.getcwd()
        folder_dir_lst = os.listdir(folder_dir)
    else:
        # print(f"{name} already exists")
        os.chdir(name)
        folder_dir = os.getcwd()
        folder_dir_lst = os.listdir(folder_dir)
    return folder_dir, folder_dir_lst


# project/src/user_end
def src_user_end():
    os.chdir(src_dir)
    lst = os.listdir(src_dir)
    return create_folder("user_end", lst)


# project/src/miner_end
def src_miner_end():
    # src_dir = os.getcwd()
    # src_lst = os.listdir(src_dir)
    os.chdir(src_dir)
    lst = os.listdir(src_dir)
    return create_folder("miner_end", lst)


# project/src/miner_end/p2p
def src_p2p():
    os.chdir(src_miner_end()[0])
    lst = src_miner_end()[1]
    return create_folder("p2p", lst)


# project/src/miner_end/ipfs
def src_ipfs():
    os.chdir(src_miner_end()[0])
    lst = src_miner_end()[1]
    return create_folder("ipfs", lst)


# project/src/miner_end/tx_verification
def src_tx_verification():
    os.chdir(src_miner_end()[0])
    lst = src_miner_end()[1]
    return create_folder("tx_verification", lst)


# project/src/miner_end/block_generation
def src_block_generation():
    os.chdir(src_miner_end()[0])
    lst = src_miner_end()[1]
    return create_folder("block_generation", lst)


# project/src/miner_end/reverse_block_verification
def src_reverse_block_verification():
    os.chdir(src_miner_end()[0])
    lst = src_miner_end()[1]
    return create_folder("reverse_block_verification", lst)


# project/output
def output():
    os.chdir(project()[0])
    lst = project()[1]
    return create_folder("output", lst)


# project/output/user_end
def output_user_end():
    os.chdir(output()[0])
    lst = output()[1]
    return create_folder("user_end", lst)


# project/output/user_end/key_pairs
def output_key_pairs():
    os.chdir(output_user_end()[0])
    lst = output_user_end()[1]
    return create_folder("key_pairs", lst)


# project/output/user_end/addresses
def output_addresses():
    os.chdir(output_user_end()[0])
    lst = output_user_end()[1]
    return create_folder("addresses", lst)


# project/output/user_end/tx
def output_tx():
    os.chdir(output_user_end()[0])
    lst = output_user_end()[1]
    return create_folder("tx", lst)


# project/output/user_end/tx_cid
def output_tx_cid():
    os.chdir(output_user_end()[0])
    lst = output_user_end()[1]
    return create_folder("tx_cid", lst)


# project/output/miner_end
def output_miner_end():
    os.chdir(output()[0])
    lst = output()[1]
    return create_folder("miner_end", lst)


# project/output/miner_end/p2p
def output_p2p():
    os.chdir(output_miner_end()[0])
    lst = output_miner_end()[1]
    return create_folder("p2p", lst)


# project/output/miner_end/p2p/receiving_block_cid
def p2p_receiving_block_cid():
    os.chdir(output_p2p()[0])
    lst = output_p2p()[1]
    return create_folder("receiving_block_cid", lst)


# project/output/miner_end/p2p/receiving_tx_cid
def p2p_receiving_tx_cid():
    os.chdir(output_p2p()[0])
    lst = output_p2p()[1]
    return create_folder("receiving_tx_cid", lst)


# project/output/miner_end/p2p/sending_tx_cid
def p2p_sending_tx_cid():
    os.chdir(output_p2p()[0])
    lst = output_p2p()[1]
    return create_folder("sending_tx_cid", lst)


# project/output/miner_end/p2p/sending_block_cid
def p2p_sending_block_cid():
    os.chdir(output_p2p()[0])
    lst = output_p2p()[1]
    return create_folder("sending_block_cid", lst)


# project/output/miner_end/ipfs
def output_ipfs():
    os.chdir(output_miner_end()[0])
    lst = output_miner_end()[1]
    return create_folder("ipfs", lst)


# project/output/miner_end/ipfs/raw_block_sending
def ipfs_raw_block_sending():
    os.chdir(output_ipfs()[0])
    lst = output_ipfs()[1]
    return create_folder("raw_block_sending", lst)


# project/output/miner_end/ipfs/raw_block_fetching
def ipfs_raw_block_fetching():
    os.chdir(output_ipfs()[0])
    lst = output_ipfs()[1]
    return create_folder("raw_block_fetching", lst)


# project/output/miner_end/ipfs/raw_tx_sending
def ipfs_raw_tx_sending():
    os.chdir(output_ipfs()[0])
    lst = output_ipfs()[1]
    return create_folder("raw_tx_sending", lst)


# project/output/miner_end/ipfs/raw_tx_fetching
def ipfs_raw_tx_fetching():
    os.chdir(output_ipfs()[0])
    lst = output_ipfs()[1]
    return create_folder("raw_tx_fetching", lst)


# project/output/miner_end/verified_tx
def output_verified_tx():
    os.chdir(output_miner_end()[0])
    lst = output_miner_end()[1]
    return create_folder("verified_tx", lst)


# project/output/miner_end/verified_tx/mempool
def verified_tx_mempool():
    os.chdir(output_verified_tx()[0])
    lst = output_verified_tx()[1]
    return create_folder("mempool", lst)


# project/output/miner_end/verified_tx/used_mempool
def verified_tx_used_mempool():
    os.chdir(output_verified_tx()[0])
    lst = output_verified_tx()[1]
    return create_folder("used_mempool", lst)


# project/output/miner_end/verified_tx/used_raw_tx_fetched_from_ipfs
def verified_tx_used_raw_tx_fetched_from_ipfs():
    os.chdir(output_verified_tx()[0])
    lst = output_verified_tx()[1]
    return create_folder("used_raw_tx_fetched_from_ipfs", lst)


# project/output/miner_end/raw_block
def output_raw_block():
    os.chdir(output_miner_end()[0])
    lst = output_miner_end()[1]
    return create_folder("raw_block", lst)


# project/output/miner_end/raw_block_cid
def output_raw_block_cid():
    os.chdir(output_miner_end()[0])
    lst = output_miner_end()[1]
    return create_folder("raw_block_cid", lst)


# project/output/miner_end/hash_block
def output_hash_block():
    os.chdir(output_miner_end()[0])
    lst = output_miner_end()[1]
    return create_folder("hash_block", lst)


# project/output/miner_end/receiver_address_list
def output_receiver_address_list():
    os.chdir(output_miner_end()[0])
    lst = output_miner_end()[1]
    return create_folder("receiver_address_list", lst)


# src_user_end()
# src_miner_end()
# src_p2p()
# src_ipfs()
# src_tx_verification()
# src_block_generation()
# src_reverse_block_verification()
# output()
# output_user_end()
# output_key_pairs()
# output_addresses()
# output_tx()
# output_tx_cid()
# output_miner_end()
# output_p2p()
# p2p_receiving_block_cid()
# p2p_receiving_tx_cid()
# p2p_sending_tx_cid()
# p2p_sending_block_cid()
# output_ipfs()
# ipfs_raw_block_sending()
# ipfs_raw_block_fetching()
# ipfs_raw_tx_sending()
# ipfs_raw_tx_fetching()
# output_verified_tx()
# verified_tx_mempool()
# verified_tx_used_mempool()
# verified_tx_used_raw_tx_fetched_from_ipfs()
# output_raw_block()
# output_raw_block_cid()
# output_hash_block()
# output_receiver_address_list()
