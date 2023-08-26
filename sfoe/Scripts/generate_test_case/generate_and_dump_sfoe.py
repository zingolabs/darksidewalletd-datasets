import argparse
import os
from generate_sfoe import generate_test_case
from get_testcase_transactions import dump_transactions_from_block_range
from get_testcase_treestates import dump_tree_states
from get_testcase_blocks import dump_block_range_to_file

def main(args):
    zcashd_url = args.zcashd_url
    dest_folder = args.dest_folder

    sfoe_test_info = generate_test_case()
    test_start_height = sfoe_test_info["testStartHeight"]
    test_end_height = sfoe_test_info["testEndHeight"]
    test_block_range = range(test_start_height, test_end_height + 1)

    # you need the tree state to the block prior to the height of the note you want to spend
    tree_state_block_range = range(test_start_height - 1, test_start_height + 1)

    transactions_folder = os.mkdir(os.path.join(dest_folder, "transactions"))

    dump_transactions_from_block_range(zcashd_url, transactions_folder, test_block_range)

    treestates_folder = os.mkdir(os.path.join(dest_folder, "treestates"))
    dump_tree_states(zcashd_url, treestates_folder, tree_state_block_range)

    testblocks_file = os.mkdir(os.path.join(dest_folder, "sfoe_blocks.txt"))

    dump_block_range_to_file(zcashd_url, testblocks_file, test_block_range)

    print(f'SFoE generated on path: {dest_folder}')
    print("Test Info:")
    print(f'{sfoe_test_info}')
    print(f'blocks for darksidewalletd: {testblocks_file}')
    print(f'tree states for this test: {treestates_folder}')
    print(f'transactions on this test case: {transactions_folder}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates SFoE dataset on the given running Zcashd regtest node')
    parser.add_argument("zcashd_url", type=str, help="The authenticated RPC url for Zcashd. Example: http://rpcuser:rpcpassword@127.0.0.1:8232")
    parser.add_argument("dest_folder", type=str, help="Path of the folder where that the data will be dumped to")
    args = parser.parse_args()
    main(args)