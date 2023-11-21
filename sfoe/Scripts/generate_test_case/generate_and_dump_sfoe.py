import argparse
import os
from generate_sfoe import generate_test_case
from get_testcase_transactions import dump_transactions_from_block_range
from get_testcase_treestates import dump_tree_states
from get_testcase_blocks import dump_block_range_to_file

def main(parser):
    args = parser.parse_args()

    zcashd_url = args.zcashd_url
    dest_folder = args.dest_folder
    test_start_height = 0
    test_end_height = 0
    skip_gen = args.skip_gen != None
    if skip_gen:
        test_start_height = args.skip_gen
        test_end_height = args.end_height
    else:
        sfoe_test_info = generate_test_case()
        test_start_height = sfoe_test_info["testStartHeight"]
        test_end_height = sfoe_test_info["testEndHeight"]
    
    if (test_end_height - test_start_height) <= 0:
        parser.print_help()
        exit(1)
    
    test_block_range = range(test_start_height, test_end_height + 1)

    # you need the tree state to the block prior to the height of the note you want to spend
    tree_state_block_range = range(test_start_height - 1, test_end_height + 1)

    transactions_folder = os.path.join(dest_folder, "transactions")
    os.mkdir(transactions_folder)

    dump_transactions_from_block_range(zcashd_url, transactions_folder, test_block_range)
    
    treestates_folder = os.path.join(dest_folder, "treestates") 
    os.mkdir(treestates_folder)

    dump_tree_states(zcashd_url, treestates_folder, tree_state_block_range)

    testblocks_file = os.path.join(dest_folder, "sfoe_blocks.txt") 

    dump_block_range_to_file(zcashd_url, testblocks_file, test_block_range)

    print(f'SFoE generated on path: {dest_folder}')
    print("Test Info:")
    print(f'start height: {test_start_height}')
    print(f'end height: {test_end_height}')
    print(f'blocks for darksidewalletd: {testblocks_file}')
    print(f'tree states for this test: {treestates_folder}')
    print(f'transactions on this test case: {transactions_folder}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates SFoE dataset on the given running Zcashd regtest node')
    parser.add_argument("zcashd_url", type=str, help="The authenticated RPC url for Zcashd. Example: http://rpcuser:rpcpassword@127.0.0.1:8232")
    parser.add_argument("dest_folder", type=str, help="Path of the folder where that the data will be dumped to")
    parser.add_argument("--skip-gen", type=int, help="provide start_height on this argument if you want to skip SFoE Generation and dump the test according to existing data on zcashd", required=False)
    parser.add_argument("--end-height", type=int, help="Height on which the test dump ends", required=False)
    
    main(parser)