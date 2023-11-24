import requests
import argparse
import json
import os

def dump_tree_states(zcashd_url, folder_path, range):
    network_name = get_network_name(zcashd_url)
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
        # transform into lightwalletd's TreeState struct format.
        json_tree_state = zcashd_tree_state_to_compact_tree_state(block, network_name)

        # write to file
        file = open(os.path.join(folder_path,f'{block_height}.json'), "w")
        file.write(json_tree_state)
        file.close()

def zcashd_tree_state_to_compact_tree_state(z_tree_state, network_name):
    tree_state = {
        "network": network_name,
        "height": z_tree_state["height"],
        "hash": z_tree_state["hash"],
        "time": z_tree_state["time"],
        "saplingTree": z_tree_state["sapling"]["commitments"]["finalState"],
        "orchardTree": z_tree_state["orchard"]["commitments"]["finalState"]
    }

    return json.dumps(tree_state, indent=4)

def get_network_name(zcashd_url):
    payload = {
        "method": "getblockchaininfo",
        "params": [],
        "jsonrpc": "2.0",
        "id": 0,
    }

    return requests.post(zcashd_url, json=payload).json()["result"]["chain"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get tree states into darksidewalletd dataset format from running zcashd instance.')
    parser.add_argument("zcashd_url", type=str, help="The authenticated RPC url for Zcashd. Example: http://rpcuser:rpcpassword@127.0.0.1:8232")
    parser.add_argument("tree_state_folder", type=str, help="Path of the folder where the tree state files will be written to.")
    parser.add_argument("start_block", type=int, help="Block Height to start from.")
    parser.add_argument("stop_block", type=int, help="Block Height to stop at.")
    args = parser.parse_args()
    dump_tree_states(args.zcashd_url,args.tree_state_folder,range(args.start_block,args.stop_block))