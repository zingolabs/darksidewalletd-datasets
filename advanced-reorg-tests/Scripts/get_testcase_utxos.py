import argparse
import json
from zcash_rpc import ZcashRPCClient

def get_address_utxos(zcash_url: str, address: str, file_path: str):
    
    rpc = ZcashRPCClient(zcash_url)

    result = rpc.get_address_utxos(address=address)

    with open(file_path, "w") as outfile:
        json.dump(result, outfile)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate the regtest base dataset for advanced reorg tests')
    parser.add_argument("zcashd_url", type=str, help="The authenticated RPC url for Zcashd. Example: http://rpcuser:rpcpassword@127.0.0.1:8232")
    parser.add_argument("address", type=str, help="Path of the file that the blocks will be written to.")
    parser.add_argument("dest_file", type=str, help="file path of the json file that will contain the results")
    args = parser.parse_args()

    get_address_utxos(
        zcash_url=args.zcashd_url, address=args.address, file_path=args.dest_file
    )
