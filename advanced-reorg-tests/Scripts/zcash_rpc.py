import requests
import time
import sys

from enum import Enum

class OpidStatus(Enum):
    SUCCESS = 1,
    PENDING = 2,
    FAILURE = 3
    
    @staticmethod
    def from_status(status):
        if status == "queued" or status == "executing":
            return OpidStatus.PENDING
        if status == "failed":
            return OpidStatus.FAILURE
        if status == "success":
            return OpidStatus.SUCCESS
        return None
        
class ZcashRPCClient:
    zcashd_url = ""

    def __init__(self, authenticated_url):
        self.zcashd_url = authenticated_url

    def get_new_account(self):
        payload = {
            "method": "z_getnewaccount",
            "params": [],
            "jsonrpc": "2.0",
            "id": 0,
        }
        result = requests.post(self.zcashd_url, json=payload).json()["result"]
        return result["account"]
    
    def get_new_address_for_account(self, account):
        payload = {
            "method": "z_getaddressforaccount",
            "params": [account],
            "jsonrpc": "2.0",
            "id": 0,
        }

        result = requests.post(self.zcashd_url, json=payload).json()["result"]
        return result["address"]
    
    def get_address_utxos(self, address: str):
        payload = {
            "method": "getaddressutxos",
            "params": [address],
            "jsonrpc": "2.0",
            "id": 0,
        }

        return requests.post(self.zcashd_url, json=payload).json()["result"]
    
    def get_addresses_utxos(self, addresses: list, chain_info: bool):
        payload = {
            "method": "getaddressutxos",
            "params":[ {
                "addresses": [addresses],
                "chainInfo": chain_info
            }],
            "jsonrpc": "2.0",
            "id": 0,
        }

        return requests.post(self.zcashd_url, json=payload).json()["result"]
    
    def get_addresses_for_account(self, addresses_count, account):
        addresses = []
        for i in range(0,addresses_count):
            addresses.append(self.get_new_address_for_account(account))
        return addresses

    def get_blockchain_info(self):
        payload = {
            "method": "getblockchaininfo",
            "params": [],
            "jsonrpc": "2.0",
            "id": 0,
        }

        return requests.post(self.zcashd_url, json=payload).json()["result"]

    def shield_coinbase(self, from_addr, to_addr, limit, policy):
        payload = {
            "method": "z_shieldcoinbase",
            "params": [
                from_addr,
                to_addr,
                None,
                limit,  
                None, # memo
                policy
            ],
            "jsonrpc": "2.0",
            "id": 0,
        }

        response = requests.post(self.zcashd_url, json=payload).json()

        return response["result"]

    def get_spendable_shielded_balance(self, account, pool, min_conf):
        payload = {
            "method": "z_getbalanceforaccount",
            "params": [
                account, 
                min_conf
            ],
            "jsonrpc": "2.0",
            "id": 0,
        }

        response = requests.post(self.zcashd_url, json=payload).json()

        pools = response["result"]["pools"]

        if pool in pools:
            return pools[pool]["valueZat"]
        else:
            return 0
        
    ## uses `z_sendmany` to send ZEC to the {recipients} list with {min_conf} and
    ## the given {policy}
    def zend_many(self, from_address, recipients, min_conf, policy):
        payload = {
            "method": "z_sendmany",
            "params": [
                from_address, # fromaddress
                recipients,
                min_conf, # minconf
                None, # default ZIP-317 fee
                policy
            ],
            "jsonrpc": "2.0",
            "id": 0,
        }

        response = requests.post(self.zcashd_url, json=payload).json()

        return response["result"]

    def generate_blocks(self, blocks):
        payload = {
            "method": "generate",
            "params": [blocks],
            "jsonrpc": "2.0",
            "id": 0,
        }
        
        return requests.post(self.zcashd_url, json=payload).json()["result"]

    def _any_pending_opid(opids):
        for op in opids:
            status = OpidStatus.from_status(op["status"])
            
            if status == OpidStatus.SUCCESS:
                continue
            if status == OpidStatus.PENDING:
                return OpidStatus.PENDING
            if status == OpidStatus.FAILURE:
                return OpidStatus.FAILURE

    def _get_failed_opid(opids):
        failed_opids = []
        for op in opids:
            if OpidStatus.from_status(op["status"]) == OpidStatus.FAILURE:
                failed_opids.append(op)
        return failed_opids

    ## waits for a collection of opids, reports result or timeouts otherwise
    ## use when there are operations that can be executed concurrently and 
    ## waited altogether.
    ## Notes: spend operations don't work properly, you could get duplicate nullifier errors
    def wait_for_opids_and_report_results(self, opids, timeout):
        payload = {
                "method": "z_getoperationstatus",
                "params": [
                opids
                ],
                "jsonrpc": "2.0",
                "id": 0,
            }
        response = requests.post(self.zcashd_url, json=payload).json()

        results = response["result"]

        while timeout > 0 and self._any_pending_opid(results) == OpidStatus.PENDING:
            print(f'waiting for opids time remaining {timeout}')
            time.sleep(1)
            timeout = timeout - 1
            response = requests.post(self.zcashd_url, json=payload).json()
            results = response["result"]

        status = self._any_pending_opid(results)
        assert timeout >= 0 and (status == OpidStatus.SUCCESS or status == OpidStatus.FAILURE)
        if status == OpidStatus.FAILURE:
            failed_opids = self._get_failed_opid(opids)

            print(f'opids failed: {failed_opids}')
            sys.exit(-1)
        return results


    ## waits of the opid, reports result or timeouts otherwise
    def wait_for_opid_and_report_result(self, opid, timeout):
        payload = {
                "method": "z_getoperationstatus",
                "params": [
                [ opid ]
                ],
                "jsonrpc": "2.0",
                "id": 0,
            }
        response = requests.post(self.zcashd_url, json=payload).json()

        result = response["result"][0]

        while timeout > 0 and (result["status"] == "executing" or result["status"] == "queued"):
            print(f'waiting for opid {opid} time remaining {timeout}')
            time.sleep(1)
            timeout = timeout - 1
            response = requests.post(self.zcashd_url, json=payload).json()
            result = response["result"][0]
        assert timeout >= 0 and (result["status"] == "success" or result["status"] == "failed")
        if result["status"] == "failed":
            print(f'opid: {opid} "{result["method"]}" failed with code {result["error"]["code"]} message: {result["error"]["message"]}')
            sys.exit(-1)
        return result