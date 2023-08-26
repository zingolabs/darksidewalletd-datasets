import requests
import argparse
import os

def _create_folder_at(path, name):
    folder = os.path.join(path, name)
    os.mkdir(folder)
    return folder

def _write_rawtx_into_file(path, txid, rawtxdata):
    file_path = os.path.join(path, txid)
    file = open(file_path, "w")
    file.write(rawtxdata)
    file.close()

def dump_transactions_from_block_range(zcashd_url, file_path, range):
    for block_height in range:
        block = get_block(zcashd_url, block_height)
        tx_ids = block["tx"]

        assert len(tx_ids) > 0 ## this should be an impossible condition
        
        block_folder_path = _create_folder_at(file_path, f'{block_height}')

        for tx_id in tx_ids:
            tx_hexdata = get_raw_transaction(zcashd_url, tx_id, 0)            
            _write_rawtx_into_file(block_folder_path, tx_id, tx_hexdata)
            

def get_block(zcashd_url, block_height):
    payload = {
            "method": "getblock",
            "params": [
                f'{block_height}',
                1
            ],
            "jsonrpc": "2.0",
            "id": 0,
        }

    response = requests.post(zcashd_url, json=payload).json()

    block = response["result"]
    return block

def get_raw_transaction(zcashd_url, txid, verbosity):
    payload = {
            "method": "getrawtransaction",
            "params": [
                txid,
                verbosity
            ],
            "jsonrpc": "2.0",
            "id": 0,
        }

    response = requests.post(zcashd_url, json=payload).json()

    raw_tx = response["result"]
    return raw_tx

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gets transactions from the blocks in the zcashd instance for a given range')
    parser.add_argument("zcashd_url", type=str, help="The authenticated RPC url for Zcashd. Example: http://rpcuser:rpcpassword@127.0.0.1:8232")
    parser.add_argument("dest_folder", type=str, help="Path of the folder where that the data will be dumped to")
    parser.add_argument("start_block", type=int, help="Block Height to start from.")
    parser.add_argument("stop_block", type=int, help="Blockheight to stop at.")
    args = parser.parse_args()
    dump_transactions_from_block_range(args.zcashd_url,args.dest_folder,range(args.start_block,args.stop_block + 1))