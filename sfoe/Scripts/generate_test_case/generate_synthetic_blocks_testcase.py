# This scripts grabs the 1204 blocks test case from regtest and creates a 
# synthetic blockchain inside a text file using `genblocks` tool from lightwalletd
import argparse
import os
import random
from pathlib import Path

def write_tx_into_file(file, tx_file_path):
    tx_file = open(tx_file_path,"r")
    tx_line = tx_file.readline()
    file.writelines([tx_line])
    file.write("\n")
    tx_file.close()

def gen_synthetic_sfoe(
        transactions_folder_path, 
        workbench_path,
        start_block, 
        stop_block, 
        test_length):
    assert start_block > 0
    assert stop_block > 0
    assert start_block < stop_block, "Start block should be smaller than stop block"
    assert test_length > 2, "test_length should be greater than 2 blocks"

    latest_test_height = start_block + test_length
    blocks_path = os.path.join(workbench_path, "sfoe_blocks")
    filler_blocks_range = range(start_block + 1, stop_block - 1)
    os.mkdir(blocks_path)
    
    block_file_path = os.path.join(blocks_path, f'{start_block}.txt')
    write_transactions_into_block_file_path(transactions_folder_path, start_block, block_file_path)
    
    for i in range(start_block + 1, latest_test_height):
        block_file_path = os.path.join(blocks_path, f'{i}.txt')

        # random block from filler blocks
        random_filler_block_height = random.randrange(filler_blocks_range.start, filler_blocks_range.stop)

        write_transactions_into_block_file_path(transactions_folder_path, random_filler_block_height, block_file_path)
    

    # write the last transaction of the test here. 

    block_file_path = os.path.join(blocks_path, f'{latest_test_height}.txt')

    write_transactions_into_block_file_path(transactions_folder_path, stop_block, block_file_path)

    print(f'Created a {test_length} blocks SFoE dataset')
    print(f'test starts at height {start_block} where "User Wallet" receives the first')
    print(f'it contains filler blocks from block {start_block + 1} to {latest_test_height - 1}')
    print(f'it contains the lastest funds for the "User Wallet" at height {latest_test_height}')

def write_transactions_into_block_file_path(transactions_folder_path, i, block_file_path):
    block_file = open(block_file_path, "w")

    block_transaction_folder = os.path.join(transactions_folder_path, f'{i}')

    # we need transaction files to be written in creation order since they are
    # dumped into the file system like that
    paths = sorted(Path(block_transaction_folder).iterdir(), key=os.path.getctime)
        
    # write the txs inside of the transactions directory to txt block file
    for tx_file in paths:
        write_tx_into_file(block_file, tx_file)
    
    # close block file
    block_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lay down the blocks in a structure that is suitable for darksidewalletd `genblocks`.')
    parser.add_argument("transactions_folder", type=str, help="Path of the folder where the tree state files will be written to.")
    parser.add_argument("workbench_path", type=str, help="Writable path for the blocks workbench folder to be placed at")
    parser.add_argument("start_block", type=int, help="Block Height to start from. This indicates the start of the first transaction of the folder you want to include")
    parser.add_argument("stop_block", type=int, help="Block Height to stop at. This indicates when the regtest SFoE test ends and it should grab the last transaction from.")
    parser.add_argument("test_length", type=int, help="the length of the test you would like to generate. Example: 10000")
    args = parser.parse_args()
    gen_synthetic_sfoe(args.transactions_folder, args.workbench_path, args.start_block, args.stop_block, args.test_length)