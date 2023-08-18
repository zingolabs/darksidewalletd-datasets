import requests
import argparse

def dump_tree_states(zcashd_url, folder_path, range):
    

    for block_height in range:
        payload = {
            "method": "z_gettreestate",
            "params": [
                f'{block_height}'
            ],
            "jsonrpc": "2.0",
            "id": 0,
        }

        response = requests.post(zcashd_url, json=payload).json()

        block = response["result"]
        file.write(block)
        file.write("\n")

    file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get blocks into darksidewalletd dataset format from running zcashd instance.')
    parser.add_argument("zcashd_url", type=str, help="The authenticated RPC url for Zcashd. Example: http://rpcuser:rpcpassword@127.0.0.1:8232")
    parser.add_argument("blocks_file", type=str, help="Path of the file that the blocks will be written to.")
    parser.add_argument("start_block", type=int, help="Block Height to start from.")
    parser.add_argument("stop_block", type=int, help="Blockheight to stop at.")
    args = parser.parse_args()
    dump_tree_states(args.zcashd_url,args.blocks_file,range(args.start_block,args.stop_block))