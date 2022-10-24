from pathlib import Path
import os

# Current directory: E:\Extra\Minhaz\Projects\Scalabale-blockchain-system\src
# Starting of this code, the location should be in src directory
# Otherwise the code will throw error or the structure of the folders will be disrupted
current_dir = Path.cwd()
# print(f"Current directory: {current_dir}")


def src():
    return current_dir


def project():
    project_dir = current_dir.parent
    return project_dir


def create_folder(name):
    if name.exists():
        # print(f"'{name}' already exists.")
        pass
    else:
        os.makedirs(name)
        # print(f"'{name}' is created")
    return name


# project/src/user_end
def src_user_end():
    src_user_end_dir = Path(current_dir) / "user_end"
    return create_folder(src_user_end_dir)


# project/src/miner_end
def src_miner_end():
    src_miner_end_dir = Path(current_dir) / "miner_end"
    return create_folder(src_miner_end_dir)


# project/src/miner_end/p2p
def src_p2p():
    src_p2p_dir = Path(current_dir) / "miner_end" / "p2p"
    return create_folder(src_p2p_dir)


# project/src/miner_end/ipfs
def src_ipfs():
    src_ipfs_dir = Path(current_dir) / "miner_end" / "ipfs"
    return create_folder(src_ipfs_dir)


# project/src/miner_end/tx_verification
def src_tx_verification():
    src_tx_verification_dir = Path(current_dir) / "miner_end" / "tx_verification"
    return create_folder(src_tx_verification_dir)


# project/src/miner_end/block_generation
def src_block_generation():
    src_block_generation_dir = Path(current_dir) / "miner_end" / "block_generation"
    return create_folder(src_block_generation_dir)


# project/src/miner_end/reverse_block_verification
def src_reverse_block_verification():
    src_reverse_block_verification_dir = Path(current_dir) / "miner_end" / "reverse_block_verification"
    return create_folder(src_reverse_block_verification_dir)


# project/output
def output():
    output_dir = Path(project()) / "output"
    return create_folder(output_dir)


# project/output/user_end
def output_user_end():
    output_user_end_dir = Path(project()) / "output" / "user_end"
    return create_folder(output_user_end_dir)


# project/output/user_end/key_pairs
def output_key_pairs():
    output_key_pairs_dir = Path(project()) / "output" / "user_end" / "key_pairs"
    return create_folder(output_key_pairs_dir)


# project/output/user_end/addresses
def output_addresses():
    output_addresses_dir = Path(project()) / "output" / "user_end" / "addresses"
    return create_folder(output_addresses_dir)


# project/output/user_end/tx
def output_tx():
    output_tx_dir = Path(project()) / "output" / "user_end" / "tx"
    return create_folder(output_tx_dir)


# project/output/user_end/used_tx
def output_used_tx():
    output_used_tx_dir = Path(project()) / "output" / "user_end" / "used_tx"
    return create_folder(output_used_tx_dir)


# project/output/user_end/tx_cid
def output_tx_cid():
    output_tx_cid_dir = Path(project()) / "output" / "user_end" / "tx_cid"
    return create_folder(output_tx_cid_dir)


# project/output/user_end/used_tx_cid
def output_used_tx_cid():
    output_used_tx_cid_dir = Path(project()) / "output" / "user_end" / "used_tx_cid"
    return create_folder(output_used_tx_cid_dir)


# project/output/miner_end
def output_miner_end():
    output_miner_end_dir = Path(project()) / "output" / "miner_end"
    return create_folder(output_miner_end_dir)


# project/output/miner_end/p2p
def output_p2p():
    output_p2p_dir = Path(project()) / "output" / "miner_end" / "p2p"
    return create_folder(output_p2p_dir)


# project/output/miner_end/p2p/receiving_hash_block
def p2p_receiving_block_cid():
    p2p_receiving_block_cid_dir = Path(project()) / "output" / "miner_end" / "p2p" / "receiving_hash_block"
    return create_folder(p2p_receiving_block_cid_dir)


# project/output/miner_end/p2p/receiving_tx_cid
def p2p_receiving_tx_cid():
    p2p_receiving_tx_cid_dir = Path(project()) / "output" / "miner_end" / "p2p" / "receiving_tx_cid"
    return create_folder(p2p_receiving_tx_cid_dir)


# project/output/miner_end/p2p/sending_tx_cid
def p2p_sending_tx_cid():
    p2p_sending_tx_cid_dir = Path(project()) / "output" / "miner_end" / "p2p" / "sending_tx_cid"
    return create_folder(p2p_sending_tx_cid_dir)


# project/output/miner_end/p2p/sending_hash_block
def p2p_sending_block_cid():
    p2p_sending_block_cid_dir = Path(project()) / "output" / "miner_end" / "p2p" / "sending_hash_block"
    return create_folder(p2p_sending_block_cid_dir)


# project/output/miner_end/p2p/used_receiving_block_cid
def p2p_used_receiving_block_cid():
    p2p_used_receiving_block_cid_dir = Path(project()) / "output" / "miner_end" / "p2p" / "used_receiving_block_cid"
    return create_folder(p2p_used_receiving_block_cid_dir)


# project/output/miner_end/p2p/used_receiving_tx_cid
def p2p_used_receiving_tx_cid():
    p2p_used_receiving_tx_cid_dir = Path(project()) / "output" / "miner_end" / "p2p" / "used_receiving_tx_cid"
    return create_folder(p2p_used_receiving_tx_cid_dir)


# project/output/miner_end/p2p/used_sending_tx_cid
def p2p_used_sending_tx_cid():
    p2p_used_sending_tx_cid_dir = Path(project()) / "output" / "miner_end" / "p2p" / "used_sending_tx_cid"
    return create_folder(p2p_used_sending_tx_cid_dir)


# project/output/miner_end/p2p/used_sending_block_cid
def p2p_used_sending_block_cid():
    p2p_used_sending_block_cid_dir = Path(project()) / "output" / "miner_end" / "p2p" / "used_sending_block_cid"
    return create_folder(p2p_used_sending_block_cid_dir)


# project/output/miner_end/ipfs
def output_ipfs():
    output_ipfs_dir = Path(project()) / "output" / "miner_end" / "ipfs"
    return create_folder(output_ipfs_dir)


# project/output/miner_end/ipfs/raw_block_sending
def ipfs_raw_block_sending():
    ipfs_raw_block_sending_dir = Path(project()) / "output" / "miner_end" / "ipfs" / "raw_block_sending"
    return create_folder(ipfs_raw_block_sending_dir)


# project/output/miner_end/ipfs/raw_block_fetching
def ipfs_raw_block_fetching():
    ipfs_raw_block_fetching_dir = Path(project()) / "output" / "miner_end" / "ipfs" / "raw_block_fetching"
    return create_folder(ipfs_raw_block_fetching_dir)


# project/output/miner_end/ipfs/raw_tx_sending
def ipfs_raw_tx_sending():
    ipfs_raw_tx_sending_dir = Path(project()) / "output" / "miner_end" / "ipfs" / "raw_tx_sending"
    return create_folder(ipfs_raw_tx_sending_dir)


# project/output/miner_end/ipfs/raw_tx_fetching
def ipfs_raw_tx_fetching():
    ipfs_raw_tx_fetching_dir = Path(project()) / "output" / "miner_end" / "ipfs" / "raw_tx_fetching"
    return create_folder(ipfs_raw_tx_fetching_dir)


# project/output/miner_end/verified_tx
def output_verified_tx():
    output_verified_tx_dir = Path(project()) / "output" / "miner_end" / "verified_tx"
    return create_folder(output_verified_tx_dir)


# project/output/miner_end/verified_tx/mempool
def verified_tx_mempool():
    verified_tx_mempool_dir = Path(project()) / "output" / "miner_end" / "verified_tx" / "mempool"
    return create_folder(verified_tx_mempool_dir)


# project/output/miner_end/verified_tx/used_mempool
def verified_tx_used_mempool():
    verified_tx_used_mempool_dir = Path(project()) / "output" / "miner_end" / "verified_tx" / "used_mempool"
    return create_folder(verified_tx_used_mempool_dir)


# project/output/miner_end/verified_tx/used_raw_tx_fetched_from_ipfs
def verified_tx_used_raw_tx_fetched_from_ipfs():
    verified_tx_used_raw_tx_fetched_from_ipfs_dir = Path(project()) / "output" / "miner_end" / "verified_tx" / "used_raw_tx_fetched_from_ipfs"
    return create_folder(verified_tx_used_raw_tx_fetched_from_ipfs_dir)


# project/output/miner_end/raw_block
def output_raw_block():
    output_raw_block_dir = Path(project()) / "output" / "miner_end" / "raw_block"
    return create_folder(output_raw_block_dir)


# project/output/miner_end/raw_block_for_ipfs_use
def output_raw_block_for_ipfs_use():
    output_raw_block_for_ipfs_use_dir = Path(project()) / "output" / "miner_end" / "raw_block_for_ipfs_use"
    return create_folder(output_raw_block_for_ipfs_use_dir)


# project/output/miner_end/raw_block_cid
def output_raw_block_cid():
    output_raw_block_cid_dir = Path(project()) / "output" / "miner_end" / "raw_block_cid"
    return create_folder(output_raw_block_cid_dir)


# project/output/miner_end/hash_block
def output_hash_block():
    output_hash_block_dir = Path(project()) / "output" / "miner_end" / "hash_block"
    return create_folder(output_hash_block_dir)


# project/output/miner_end/receiver_address_list
def output_receiver_address_list():
    output_receiver_address_list_dir = Path(project()) / "output" / "miner_end" / "receiver_address_list"
    return create_folder(output_receiver_address_list_dir)


def main():
    # output_receiver_address_list()
    # output_hash_block()
    # output_raw_block_cid()
    # output_raw_block()
    # verified_tx_used_raw_tx_fetched_from_ipfs()
    # verified_tx_used_mempool()
    # verified_tx_mempool()
    # output_verified_tx()
    # ipfs_raw_tx_fetching()
    # ipfs_raw_tx_sending()
    # ipfs_raw_block_fetching()
    # print(f"src dir: {src()}")
    # print(f"project dir: {project()}")
    # src_user_end()
    # src_miner_end()
    # src_p2p()
    # src_ipfs()
    # src_tx_verification()
    # src_block_generation()
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
    pass


main()