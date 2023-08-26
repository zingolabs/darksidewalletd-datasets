# Addresses involved
USER_ADDRESSES = [
    "uregtest19sufy4qyv6f52773a3tklff0muzwjyv3hlqjvtp6z8spwf6xteksr5u7gmdv6h5g6wpz0flaeutxcaqqwwafffhvqetudsvfe7mtnn62yuzv77uv7azskfrqd6dqyz0zhms3yn2wjd82dqetgzddc6h0kf0t3jphenc3ts62jmcsh83ra2nj0fqeuuflq6a6asaq4fjdrzhlq5w7twd",
    "uregtest1drpsp4tde5tc2cygdkh3qf42panvmrldzr3jmnd8xcvd2xcje39fufxe02xnte9j8uhed2cx39cpt2fr7m6xfhgx8y3ttpvx5f3ll8ygjjc257dpmtuwy6t9stdk9rvf5uxws9ynu2m0kud9kdkqlrqyr6eh58pfr7yy44jn9qqcvmwkr935822ynnhcuup2m2neqfh734whvkwnqc0",
    "uregtest1vvh6cuhhgygxgzcsuzl9rmxsk5hnk2axvchfw7e63y00yxjqmw3l694rtg0syzjmkwemx0ue46sejcjyyr8768qtxay9xq53hnth8et4ns449zrhtl797pr3dt2fm3x8lyt8ctxvsdr5f2ql4p5nry3pw3ph76aceam6qedtvgy38achk6vgwv4749w3dkczetphhxq9sjemwts360p",
    "uregtest1zsgf2s5w6nur99vt6feavywx2mv3j08xmamrzztuttj6wwlezkp0cy0x840ct7083qx8drqpknmv2nqcj3p7q2fu6zjzhr6j2nvmcp5255qmqqdhp68ztt4p99xn8p0fz2t7uvga4ts8sz26pa993pgsdvwye9whygx399jmhlldtm3vgcc4d7ts6nadgy2k0efl5k3s6jmtsr09742",
    "uregtest1xz72fz2ah3v068xkymzf3l3zj90vf4f82wrru8gwcyezxw4dem6vx6vaf3hlnntjguz42hd0j2eegzmjj0qyudr26cfx7ku5efx39s8azscdjuw9tyz84dh4a4yne9wswlcncvcsjv3f89w4ejy62xqezl6f3qa3yn2c5ju2lvdk3r0exn49aacge78c65vpdl9wdac2qwtxwa3svjz",
    "uregtest1p9m4q6lvu8sq8jxy7mjzhdu5u5eedmn8uqrlfp6z4fdma5may5c6lgmh9mqhlgc0y7qmue6y77mvjdgljhacfcktwu7lrrylgp93hny72ur3a5j3mrmwnw2kzjscv4excl7pqujsdkxtlhjdqw6qapz7y4fawsgyqdp0mfptmme9arlyqzq6v9ktghqnamjuu55zdlhpy0tgxz9xstn",
    "uregtest109a97fj92sr42lcyqmvu5xe3eew4k9lnuhgxz8u8l4p930xtk2r3w25fvkxravwr4ps6xrrche8xagpq698cvjla8ljh2e924papzuysuj5ugkz7kjuhy6skd92m97wxj4usdp8ayjn4w4qvyf8zjtmauu0nxcw7ss7pethv8w0zrc6fxeck5x72vndqyqq36cwq597mn2czs8jpqwr",
    "uregtest164uq5s4rnrvwv3z67vhrggu4mwgrvjady30nlszdz35ftt2gr8la39nnhm68rmq9wd0aqwzfshd0shjjk4y24dh9q9hs0ccx5lrh87c30z5qs0ml68en0vnhaagdmsn7nw6u9wr80vxv23zrljz06cyhdvrs7s50kzcx0jjwwd9nwk22yz97hslt0xakf3jvvz8f0h3yt5d9z72acku",
    "uregtest1kntestpv5s57h4uj8sqln8xrkejgcfsujkgtteeqtg4d5g2gxrxtch5ep9pu792hhnzqnslt0hjx495ykdhzx2005e7pm8dkenkk6mvj9tjrphwlfgl0cc6fngn48cprx44d0wskh3r9n42gx67u0hzxvd6fkd773rpxj47fmkt3ql7ncv5tdwy5z7g5jpms5rwpflqdd7ggc8rf720",
    "uregtest1f8qps9vl96wdgxh6650qlemmcppye93k42czjfhg8u7xea2vs49us0mzj7g8p925msg9xrmpf3pfgd36fjfvcpy2gwkm4uh328wl3lw62qgtyxzxg4jwhhs23n0wnkz7cgfghmmhd9d7v0sc7t7n6yxgruxqrpuk0ytr77yshzy2esu3plgzu4pqduexz0zqahfe7qpqk08gqksvurq"
]

FILLER_ADDRESSES = [
    "uregtest1fl28qdx08zgweef5ve4usg3u2fan5cgth7rnc77wkq5rm8az8rluct727p58vfm64r5zkj90aqmd9rlatqnalkh0zrmw4sy6sgaex3gnux3ahkq3lr542nlags0l2ax257clhdwkqcps2pjxnmawgzqdfpeuqtch889ml9dfmqeq0zapkgw86hzs5sfj3s3vgnt477a7x25c7yjr62j",
    "uregtest1z8s5szuww2cnze042e0re2ez8l3d04zvkp7kslxwdha6tp644srd4nh0xlp8a05avzduc6uavqkxv79x53c60hrc0qsgeza3age2g3qualullukd4s0lsn6mtfup4z8jz6xdz2c05zakhafc7pmw0dwugwu9ljevzgyc3mfwxg9slr87k8l7cq075gl3fgxpr85uuvxhxydrskp2303"
]

FILLER_BLOCK_COUNT = 2
# Config stuff
RPCUSER = "pacu"
RPCPASSWORD = "pacu"
POLICY = "FullPrivacy"
ZCASHD_URL = "http://pacu:pacu@127.0.0.1:8232"

import requests
import time
import sys
import json

def get_new_account():
    payload = {
        "method": "z_getnewaccount",
        "params": [],
        "jsonrpc": "2.0",
        "id": 0,
    }
    result = requests.post(ZCASHD_URL, json=payload).json()["result"]
    return result["account"]

def get_new_address_for_account(account):
    payload = {
        "method": "z_getaddressforaccount",
        "params": [account],
        "jsonrpc": "2.0",
        "id": 0,
    }

    result = requests.post(ZCASHD_URL, json=payload).json()["result"]
    return result["address"]

def get_addresses_for_account(addresses_count, account):
    addresses = []
    for i in range(0,addresses_count):
        addresses.append(get_new_address_for_account(account))
    return addresses

def get_blockchain_info():
    payload = {
        "method": "getblockchaininfo",
        "params": [],
        "jsonrpc": "2.0",
        "id": 0,
    }

    return requests.post(ZCASHD_URL, json=payload).json()["result"]

def main():
    # get blockchain info
   
    info = get_blockchain_info()
    chain = info["chain"] 
    blocks = info["blocks"]
    commitments = info["commitments"]

    assert chain == "regtest"
    assert blocks == 0
    assert commitments == 0

    
    print("Zcashd regtest ready on zero blocks")

    print("generate account 0")

    account = get_new_account()

    print(f'generate new address for account {account}')

    miner_addresses = get_addresses_for_account(100, account)

    print("generating First 200 blocks")

    blockhashes = generate_blocks(200)

    assert len(blockhashes) > 0
    
    print(f'Generated block hashes {blockhashes}')

    # shield the mature coinbases
    shielded_op_id = shield_coinbase(
        "*",
        miner_addresses[0],
        1, # one coinbase
        "AllowRevealedSenders"
    )
    
    print(f'shielded coinbase {shielded_op_id}')

    wait_for_opid_and_report_result(shielded_op_id["opid"], 10)
    # mine the shielded coinbases
    print(f'generate 1 block {generate_blocks(1)}')

    time.sleep(1)

    shielded_op_id = shield_coinbase(
        "*",
        miner_addresses[0],
        1, # one coinbase
        "AllowRevealedSenders"
    )
    
    print(f'shielded coinbase {shielded_op_id}')

    wait_for_opid_and_report_result(shielded_op_id["opid"], 10)

    # mine the shielded coinbases
    print(f'generate 1 block {generate_blocks(1)}')

    time.sleep(1)

    shielded_op_id = shield_coinbase(
        "*",
        miner_addresses[0],
        1, # one coinbase
        "AllowRevealedSenders"
    )
    
    print(f'shielded coinbase {shielded_op_id}')

    wait_for_opid_and_report_result(shielded_op_id["opid"], 10)
    
    # mine the shielded coinbases
    print(f'generate 1 block {generate_blocks(1)}')

    time.sleep(1)

    shielded_op_id = shield_coinbase(
        "*",
        miner_addresses[0],
        1, # one coinbase
        "AllowRevealedSenders"
    )
    
    print(f'shielded coinbase {shielded_op_id}')

    wait_for_opid_and_report_result(shielded_op_id["opid"], 10)
    
    shielded_op_id = shield_coinbase(
        "*",
        miner_addresses[0],
        1, # one coinbase
        "AllowRevealedSenders"
    )
    
    print(f'shielded coinbase {shielded_op_id}')

    wait_for_opid_and_report_result(shielded_op_id["opid"], 10)

    # mine the shielded coinbases
    print(f'generate 1 block {generate_blocks(1)}')

    time.sleep(1)
    shielded_op_id = shield_coinbase(
        "*",
        miner_addresses[0],
        0, # all coinbases
        "AllowRevealedSenders"
    )
    
    print(f'shielded coinbase {shielded_op_id}')

    wait_for_opid_and_report_result(shielded_op_id["opid"], 20)
    # mine the shielded coinbases
    print(f'generate 1 block {generate_blocks(1)}')
    time.sleep(1)
    print(f'generate 1 block {generate_blocks(1)}')
    time.sleep(1)

    # break the balance of miner wallet in smaller notes
    #print("break the balance of miner wallet in smaller notes")
    #op_ids = break_shielded_balance_into(addresses=miner_addresses, fractioned_value=0.1,  account=account, rounds=10)

    #print(f'value broken into op-ids \n {op_ids}')

    # generate some blocks so that the Tx breaking the balance are mined
    #print(f'Generated blocks: [ \n {generate_blocks(10)} \n]')

    sfoe_start = get_blockchain_info()["estimatedheight"]
    filler_block_count = FILLER_BLOCK_COUNT
    print(f'SFoE starting at height {sfoe_start}')
    # first z_sendmany
    # 10 unspent commitments for User wallet
    # 2 filler outputs for filler wallet

    payload = {
        "method": "z_sendmany",
        "params": [
            miner_addresses[0], # fromaddress

            # amounts
            [  # note 1
               {
                   "address": USER_ADDRESSES[0],
                   "amount" : 0.1
               },
               # note 2
               {
                   "address": USER_ADDRESSES[1],
                   "amount" : 0.1
               },
               # note 3
               {
                   "address": USER_ADDRESSES[2],
                   "amount" : 0.1
               },
               # note 4
               {
                   "address": USER_ADDRESSES[3],
                   "amount" : 0.1
               },
               # note 5
               {
                   "address": USER_ADDRESSES[4],
                   "amount" : 0.1
               },
               # note 6
               {
                   "address": USER_ADDRESSES[5],
                   "amount" : 0.1
               },
               # note 7
               {
                   "address": USER_ADDRESSES[6],
                   "amount" : 0.1
               }, 
               # note 8
               {
                   "address": USER_ADDRESSES[7],
                   "amount" : 0.1
               }, 
               # note 9
               {
                   "address": USER_ADDRESSES[8],
                   "amount" : 0.1
               }, 
               # note 10
               {
                   "address": USER_ADDRESSES[9],
                   "amount" : 0.1
               },
               # filler note 1 
               {
                   "address": FILLER_ADDRESSES[0],
                   "amount" : 0.0001
               },
               # filler note 2
               {
                   "address": FILLER_ADDRESSES[1],
                   "amount" : 0.0001
               }
            ],
            1, # minconf
            None, # default ZIP-317 fee
            POLICY
        ],
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(ZCASHD_URL, json=payload).json()

    opid = response["result"]

    # this needs a bit more of time.
    wait_for_opid_and_report_result(opid, 1000)

    assert len(opid) > 0

    print(f'Sent Txid: {opid}')

    # generate a block to 
    # start generating filler blocks
    print(f'generate 1 block {generate_blocks(1)}')
    time.sleep(1)

    print("start generating filler blocks")

    for x in range(0,FILLER_BLOCK_COUNT):
        print(f'filler block {x + 1}')

        from_address = miner_addresses[x % len(miner_addresses)]
        # generate a transaction for filler wallet
        filler_tx_1_opid = send_filler_transaction(from_address, FILLER_ADDRESSES[0])
        print(f'sent filler transaction 1 opid {filler_tx_1_opid}')
        wait_for_opid_and_report_result(filler_tx_1_opid, 10)

        time.sleep(1)

        filler_tx_2_opid = send_filler_transaction(from_address, FILLER_ADDRESSES[1])
        print(f'sent filler transaction 2 opid {filler_tx_2_opid}')
        wait_for_opid_and_report_result(filler_tx_2_opid, 10)
        
        # generate block
        new_blocks = generate_blocks(1)

        time.sleep(1)
        print(f'Generated filler block {new_blocks[0]}')

    # generate a transaction with 2 unspent note commitments for user wallet

    payload = {
        "method": "z_sendmany",
        "params": [
            miner_addresses[0], # fromaddress

            # amounts
            [  # note 1
                {
                    "address": USER_ADDRESSES[0],
                    "amount" : 0.1
                },
                # note 2
                {
                    "address": USER_ADDRESSES[1],
                    "amount" : 0.1
                }
            ],
            1, # minconf
            None, # default ZIP-317 fee
            POLICY
        ],
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(ZCASHD_URL, json=payload).json()

    opid = response["result"]

    wait_for_opid_and_report_result(opid, 15)
    
    # generate block
    new_blocks = generate_blocks(1)

    time.sleep(1)
    # validate. 

    after_info = get_blockchain_info()
    sfoe_end = after_info["blocks"]
    assert sfoe_end == 210

    test_description = {
        "testStartHeight": sfoe_start,
        "testEndHeight": sfoe_end,
        "fillerBlockCount": filler_block_count
    }

    print(f'Generation of SFoE Finished!')
    print(f'{json.dumps(test_description)}')

def shield_coinbase(from_addr, to_addr, limit, policy):
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

    response = requests.post(ZCASHD_URL, json=payload).json()

    return response["result"]

def get_spendable_shielded_balance(account, pool, min_conf):
    payload = {
        "method": "z_getbalanceforaccount",
        "params": [
            account, 
            min_conf
        ],
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(ZCASHD_URL, json=payload).json()

    pools = response["result"]["pools"]

    if pool in pools:
        return pools[pool]["valueZat"]
    else:
        return 0


## Spends all available shielded balance into the given addresses
## with the provided fractioned value
def break_shielded_balance_into(addresses, fractioned_value, account, rounds):
    op_ids = []
    spendable_balance = get_spendable_shielded_balance(account, "orchard", 1)

    for i in range(0,rounds):
        if spendable_balance <= 0: return op_ids
        # orchard max recipient count is 50 but is too much to process for a docker box
        recipient_count = min(10, round(spendable_balance / fractioned_value))
        recipients = gen_recipients(recipient_count, addresses, fractioned_value)
        op_ids.append(
            zend_many(addresses[0], recipients, 1, POLICY)
        )
        
        generate_blocks(1)

        spendable_balance = get_spendable_shielded_balance(account, "orchard", 1)
    
    return op_ids

## Generates recipient list of size {count} doing a round-robin distribution of {value} ZEC  
## over the {addressses} given 
def gen_recipients(count, addresses, value):
    recipients = []
    for i in range(0,count):
        recipients.append(
            {
                "address": addresses[i % len(addresses)],
                "amount": value
            }
        )
    return recipients

## uses `z_sendmany` to send ZEC to the {recipients} list with {min_conf} and
## the given {policy}
def zend_many(from_address, recipients, min_conf, policy):
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

    response = requests.post(ZCASHD_URL, json=payload).json()

    return response["result"]

def send_filler_transaction(from_address, to_address):
    payload = {
        "method": "z_sendmany",
        "params": [
            from_address, # fromaddress
            # amounts
            [  # note 1
               {
                   "address": to_address,
                   "amount" : 0.0001
               }
            ],
            1, # minconf
            None, # default ZIP-317 fee
            POLICY
        ],
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(ZCASHD_URL, json=payload).json()

    return response["result"]

def generate_blocks(blocks):
    payload = {
        "method": "generate",
        "params": [blocks],
        "jsonrpc": "2.0",
        "id": 0,
    }
    
    return requests.post(ZCASHD_URL, json=payload).json()["result"]

def dump_block_range_to_file(file_path, range):
    file = open(file_path,"w")

    for block_height in range:
        payload = {
            "method": "getblock",
            "params": [
                f'{block_height}',
                0
            ],
            "jsonrpc": "2.0",
            "id": 0,
        }

        response = requests.post(ZCASHD_URL, json=payload).json()

        block = response["result"]
        file.write(block)
        file.write("\n")

    file.close()

## waits of the opid, reports result or timeouts otherwise
def wait_for_opid_and_report_result(opid, timeout):
    payload = {
            "method": "z_getoperationstatus",
            "params": [
               [ opid ]
            ],
            "jsonrpc": "2.0",
            "id": 0,
        }
    response = requests.post(ZCASHD_URL, json=payload).json()

    result = response["result"][0]

    while timeout > 0 and (result["status"] == "executing" or result["status"] == "queued"):
        print(f'waiting for opid {opid} time remaining {timeout}')
        time.sleep(1)
        timeout = timeout - 1
        response = requests.post(ZCASHD_URL, json=payload).json()
        result = response["result"][0]
    assert timeout >= 0 and (result["status"] == "success" or result["status"] == "failed")
    if result["status"] == "failed":
        print(f'opid: {opid} "{result["method"]}" failed with code {result["error"]["code"]} message: {result["error"]["message"]}')
        sys.exit(-1)
    return result

if __name__ == "__main__":
    main()
