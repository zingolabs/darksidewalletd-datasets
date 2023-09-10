import json
import time
from zcash_rpc import ZcashRPCClient
import argparse

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


def generate_test_case(zcashd_url, block_count):
    rpc_cli = ZcashRPCClient(zcashd_url)
    # get blockchain info
   
    info = rpc_cli.get_blockchain_info()
    chain = info["chain"] 
    blocks = info["blocks"]
    commitments = info["commitments"]

    assert chain == "regtest"
    assert blocks == 0
    assert commitments == 0

    user_transactions = []
    filler_transactions = []
    print("Zcashd regtest ready on zero blocks")

    print("generate account 0")

    account = rpc_cli.get_new_account()

    print(f'generate new address for account {account}')

    miner_addresses = rpc_cli.get_addresses_for_account(100, account)

    print("generating First 101 blocks")

    blockhashes = rpc_cli.generate_blocks(101)

    assert len(blockhashes) > 0
    
    print(f'Generated block hashes {blockhashes}')

    time.sleep(2)
    # shield the mature coinbases in 0 subsequent blocks
    for i in range(100, 111):
        shielded_op_id = rpc_cli.shield_coinbase(
            "*",
            miner_addresses[0],
            1, # one coinbase
            "AllowRevealedSenders"
        )
        
        print(f'shielded coinbase {shielded_op_id}')

        rpc_cli.wait_for_opid_and_report_result(shielded_op_id["opid"], 11)

        # mine the shielded coinbases
        print(f'generate 1 block {rpc_cli.generate_blocks(1)}')

        time.sleep(1)

    rpc_cli.generate_blocks(90)

    start_height = rpc_cli.get_blockchain_info()["estimatedheight"]

    for x in range(0,block_count):
        print(f'Test block {x + 1}')

        from_address = miner_addresses[0]
        # generate a outputs for filler wallet
        
        filler_0_recipient = recipient(address=FILLER_ADDRESSES[0], amount=0.0001)
        filler_1_recipient = recipient(address=FILLER_ADDRESSES[1], amount=0.0001)
        
        recipients = [filler_0_recipient, filler_1_recipient]
        
        # add an output for the user wallet every 3 blocks
        if (x % 3) == 0:
            recipients.append(recipient(USER_ADDRESSES[0], 1, f'Transaction {x % 3} to user wallet address 0'))
        
        # generate block
        user_tx = rpc_cli.zend_many(from_address=from_address, recipients=recipients,min_conf=1, policy="FullPrivacy")

        result = rpc_cli.wait_for_opid_and_report_result(user_tx, 30)

        new_blocks = rpc_cli.generate_blocks(1)

        time.sleep(1)

        if (x % 3) == 0:
            user_transactions.append(result["result"]["txid"])
            print(f'Generated user tx block {new_blocks[0]}')
        else: 
            filler_transactions.append(result["result"]["txid"])
            print(f'Generated filler tx block {new_blocks[0]}')
    
    end_height = rpc_cli.get_blockchain_info()["estimatedheight"]
    test_description = {
        "testStartHeight": start_height,
        "testEndHeight": end_height,
        "blockCount": block_count,
        "userTransactions": user_transactions,
        "fillerTransactions": filler_transactions,
    }

    print(f'Generation of Advanced ReOrg Base Dataset Finished!')
    print(f'{json.dumps(test_description)}')

    return test_description

def recipient(address: str, amount: float, memo: str = None):
    if memo == None:
        return {
            "address": address,
            "amount": amount
        }

    return {
        "address": address,
        "amount": amount,
        "memo": memo.encode("utf-8").hex()
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate the regtest base dataset for advanced reorg tests')
    parser.add_argument("zcashd_url", type=str, help="The authenticated RPC url for Zcashd. Example: http://rpcuser:rpcpassword@127.0.0.1:8232")
    parser.add_argument("filler_block_count", type=int, help="Path of the file that the blocks will be written to.")
    args = parser.parse_args()

    generate_test_case(zcashd_url=args.zcashd_url, block_count=args.filler_block_count)