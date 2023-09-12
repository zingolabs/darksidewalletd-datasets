# Advanced ReOrg Tests

This is a set of tests originated as part of integration testing of the [ECC Mobile SDKs](https://github.com/zcash/ZcashLightClientKit/blob/main/Tests/DarksideTests/AdvancedReOrgTests.swift)

## Base dataset

The python script [base dataset](Scripts/generate_base_dataset.py) generates a
set of around a 100 blocks that contains transactions to the User Wallet and
to other wallets that are not subject of these tests.

### Dataset structure
`start_height`: is the height on which the test dataset starts
`end_height`: is the height on which the test dataset ends.
`userTransactions`: transactions that include outputs for the User Wallet
`filler transactions`: transaction that include only outputs that are for other wallet


All the transactions are provided independently so that developers can also use
them for their own tests if needed.

The test uses orchard funds, sapling and transparent funds

```json
{
    "testStartHeight": 202,
    "testEndHeight": 302,
    "blockCount": 100,
    "userTransactions": [
        "f58dc25a938d6eb9b3c1aee4ba733ad5d457a3b2262abdab1fafebc4cd4e023b",
        "def0d105ec08b51a573c2025978a87f2494cd9c7679e85a8443c4b05dbaad31a",
        "cf59b5ddd7b8d740059b88b9f8c2b1856755cd596751a6ba8b2f10461602a2ee",
        "2f7ec7619cdfff7a3a923181b32273e8f10e2d472a561c54fef8690787bb3983",
        "c280c4b87ba13ca41496ec1eb84ba30fbd6c5e2e8c3b2cdcf51a3c515bda050d",
        "ddbf7192d11244504938d29d8c27c706da421fd9695d8f0f017742709ee36af8",
        "be3fa09465e1533695aa3230e0cda66aa2804b3d0dfa24cd70e692be8fb41a1f",
        "0653b0cf97741eb7c9720186bad91b94135012aa4c1ea322027a9b7193f09473",
        "83449f15ace53f86107da07449c589ee3e54e7b690f56bde8dc42e05343edea6",
        "9f757b07f7b154200d39337bf249019cf0c07893c2172dca42637c19a9ddadc6",
        "1e26959001a4b4003c9d8e5254f609691f288d006186fc18095b182a3faa925c",
        "d012ad8c409e45e2e7ab2d8f098265a80873479a20bb138e09d511761ecdca69",
        "b7d4ee1cdf31a8cb31e67156880fd94f3beb1db1e292c009f3b811d6d31fd248",
        "990ab9b8415a11ffe5ff02c92be68454df4d70ee59a3b0f86be14a6f873ac6b9",
        "eb0ec8a2f330746453fbbcc5528753b03f67418a49735190169765a6300cb922",
        "8e52b75e77aed16ced73ee1de3655839898c977789a70742e66f5ad8325f781f",
        "ff3486c3284d95354d2dae2aa758c9e1858b3cb7c4835c88e2a89eb608451310",
        "5e8f2e03ddadb96e2681d8ba105a67ed1d27ca341736db8678c68dd8e830ba94",
        "97d461391bded1a5a64a85e38405fbf854d873d2d448ea964433282817e6854a",
        "c94255fdf67f5d8503e81145290bfe23855747bfd3c39a2a03fb85034da0d626",
        "8a6a12b4630e9f7db8f09f40ec68355263b37255f98afe6c06d66089394b9b8e",
        "b91cabc20b464e144d9495c44ee3254b2de1701d90a327e4b737e8600f8511f9",
        "994c386fa876ec3b39158dbedfb3e75e66b7bc75093064c525471f8be1ef789c",
        "8e89574d0aa46bfa6e5159adbb266f57159f85bc3cb40c9ca11df20749f0dcb2",
        "d8bc529b9234c2b32ce15f5f1037d28fe7c849c5d7cfd362c36dce06f408f3ab",
        "6b9d44c934e566e88d87206f9b498cb890e9c9c05475fea95d390401e1f909a2",
        "81643dc07958741481ffc7e109f59a33f7568579b404f7d2826e4593a445e993",
        "caded62679949471c8b1181457a793507966132fccebbc14488c188ce4b564b5",
        "e094b62e9828a62361e054e3b1f340988f14099e08529c27cf8394156e7f05e6",
        "69b8a27d6bde3c3296cde917e4057ee9f637d42d97965a305d7000fa04a27112",
        "1cd01965591c8ef27d6c08fa5a3433c52df89e55fc5e7ab9246e3f34a57c02f2",
        "a8cbf67e59abf30b6cd8de4429d9819896e9bbad37bca2f0bb284ff33cc1e869",
        "06e56bbf7658d3d77076ad2c6f27de74aeb3191da95f978064e2bac750fe5164",
        "0095df0f736b7b0b677bedd9a2e37fd513051e826b605bc78702fa92e3da61df",
        "32df04ee316fb22c56cfdc42f111b2fb8e680994b18d44805177fe1e35deab3b",
        "5ee9faabb528771dbf3f0725fe541dd0c19071bd0d63640576f2d040551b6430",
        "0ffc556cbffddcd43dceffd066e50fde442f643fe8f9e84295545f74a3998b4b"
    ],
    "fillerTransactions": [
        "193d6b5ac44f80e0f1b9e95930cc44d7e63a588fd9d63f6816f652cf672225f9",
        "078df7d92cfd2f6df373a8f4239963ab506890d99b9653d4e9b9145da3757faf",
        "a72ef99384b5509c30db946550474f72decb19fc76a75d0244115fab3d1dc6dd",
        "a929338a11a1ed7b9140b4c1b5431fe80e08601ffc518922dea323b335f1dec1",
        "0e600e7163dbbbc6fa63ff87479236107d6cd294964b54fa50c04423afa4ded5",
        "b12939f0820240d652a14a2c265ce3bda2ec0aa2993deb50badec90241f45a00",
        "a68753f5473168db530ae613f8f73b00838eed0e6b03b739fc6bb44ef730d592",
        "9e1531661fd901415e3fe64bd744c61f0ffc200ac3444d06a3437eb0cb3eb167",
        "87158fe093cb03436319678b48c980662d051a63b863c612be7d3b412c6b8465",
        "a308d7ef85235fbe8e0fb0ad20740be17edc0149e69ece7eb3e5eca0e5fe1ffd",
        "eb48a21464c50c6b4c0944d27c809cdbf7b67a4763cecd2fdf97074cfae0da6c",
        "55825e7fc24009b3ddc5f8e7968f3c60ef82663c08319654f1120f2bcee0bc09",
        "841628a0f9bc464cd3d323a3e1a45abac51ee231e85f5ef6bb423f0a14d6d839",
        "6a863964632a19c2b6e2f9e35d67948f87e860b89ed04f05b8d08e7b6c59f222",
        "0c98d3ea71fee04b6cbbdadc16d5f94c683534f40acee5ca6db79bb4c7b70006",
        "fe1c4639e475edf5797f7bb9af75e4313625e76036d48006dd7cf52b772a1325",
        "95b6c3b438d64b85c43b4c8b70de758a806baead3669b1c9b3b79a072f73560f",
        "e70aa1ef76ae27f7486912c85bbf0a1934ccd3ee0f5abed9eac5919f98ad0a5a",
        "8e65b1e91b283b6a931880f33584151b2f84ba263fd55bfffa673adeced439fd",
        "e2a7f92da4393cfdff7b78f0457fb40a81c1fdda0daee93f7df7e95d2ca59389",
        "4d432f40e6876597205de45d1621f4103ab0fefdd3331d83be5dc45474a7ced5",
        "2d795327aa12a34f8ae1d4d4e807b3cc983a376a10ddc32cdbe68addeed44f96",
        "9ae1bf0d1fbe6c73f095749bd2c68353fcc9912545aa7988fec978e4e1d78404",
        "a1a5fb71d6691c2681cff0080d70d59c0c0221626aab71865f7f5c3edcad2abb",
        "e2eaa79e90873de6cdb62bc91825377cc2e5f668a638f92f669242c326662f67",
        "67e1177f1c02e8645db62c4060217b94598f577620183d7b5a9a195008119283",
        "f1ce24682dce5bb8a5b6307a531e590b5672af49d60bda31f18a76e252f8aabd",
        "1cb0517fdf10940ad731253727942064d1f02e21b20dd6f685908978e18c85cb",
        "e60ef0b132a3b0383d8090158c5699a1438b9591f1df59dd4486471c35352ae5",
        "251ac98774b5ebd0e6e27e80999a5f1b629ff9efa7f55fabed5893cf63f5d90c",
        "ce33691667f862aa0064404b613646a9c0977a88f5c0d48d215aa168d53a8956",
        "b1ffe64f6957b69bdbd6bcbc2831428ad5ccf6f88ed269c46f7ffd706b4d2696",
        "911df245bb93bb0fd7f4f9876c80d66a33233ec290f47483659b318ed272ae2a",
        "be2161555df3d025eeccd4eb1a67f4aa9c2a96758036e980b5e752a9a2741378",
        "70a38de6d5766017c78b67abd690bb20e3f34b6339abdf1d48e747bc681c6b52",
        "d6360df89cf385692696bfd433e2be1420d1b95d8fdba8c23785de63d0635054",
        "5a76e54300c493686ef0f5762d389e7e8c3bd6a2055a41ec59228d481eff7dbb",
        "94e860383494d70174b4da3ccb7ef288a40acda31c9006389371e0671a085dbc",
        "625382dbeaa7d577b6282d9717602eb30cb234449f58b65514c91da3ba17fd4d",
        "30f9ca071694941da5ca5f0f1eb99b4ee0438a553e661f864da7880a0ad95813",
        "aa3f33ce5a6b4b7b432a16e532962240066d8eb09931612ff496eab240e79de2",
        "102a1c10377198fa449661de97ae8a05ae4dfcb721bd339b3cd87f30edaef63c",
        "158426f27cb2a58eabbe1e20f6e71676813e6530bbe7a1aa366f5e8ee37d826d",
        "e9408b1bd38356db6a8aa67833368867f7de5858e2afef01c4e08d784afaf0a6",
        "686e83b7f6c5d5997ec4c955ea5aa44559d485e516319923bb467b02443433f3",
        "11d133ac5b747ba33b7728c477d0d8aec41a42fedeb9cefb352dd803eefde908",
        "4e7eabe5e88ea9b09377c4fd951a43ece968b2dcf62fbbf5e20db9128da9fb6a",
        "2645cf113e6388015e7137264f18858f327c36099a41e1346aed66f213bfdc0d",
        "a4493c91bc21bcd85c96524330d94fc36b9794178dd71862a4c9d63c8343af06",
        "980c3da0c0f2a20e5eda641ad74c0eed54cd8422ec0e4a8daf74fa271f22011a",
        "ab53f8523b264748de3ec9b615f11f2c574e8e47f54f74e4b020ef750e9fce8d",
        "a6bbc16a972487de65cd72849099ecf32e7858a686a29889c73b73ab0418be74",
        "57e95fdd19aa62892c71010dd6830d25d812d1ce849943cbfff7eb8a25f6132c",
        "734fdc0bf0952ce3664da7868ed7f1da8037172d18fd7c4af7fc6882df7cf087",
        "77a05f1710f555a2ff97914242e2d3b7c3522adbc0d7a7eeeb836a3a1bf53124",
        "5bfd9e93ab499118ae9a6d25272f67b9c2209befb1ec416b180a99ecb8cb83ce",
        "ebdc222960f2e49f1bf49c8d74813f916e246864c52ed574da8675bc869a3da8",
        "332e53cd6aa9c3f410fa151f23520e77f6c777acebe0ac357ccc629fd358996d",
        "0c5f022b9fbfaccdab9754ca15901b798cf23e4cd954ac8b73bcb57fd16152bc",
        "f23fafd7e4a888659115f53b4207e5ae2d37d5cccdcd5cc2bd589d9408ed565f",
        "1e630838a0da4b571e8ee61063113cdac36c5b2f19b2e8a528f01f441180df73",
        "c3bc3db40be03b37c997c0d6a78301a6c161ccf9ec6442b9d39117aa0446d121",
        "aae125b6242d2c45a2fbc22a949485175ed5467d47ff025a2cd098fa2714e587"
    ]
}
```


#### Folder Structure
```
dataset/
   transactions/ -> the transactions ordered by blockheight
   treestates/ -> the tree states of the dataset
   utxos/ -> utxo json files by t-address
   base_dataset_100.txt -> the dataset containing all generated transactions and blocks
```

## Recreating / Regenerating this dataset

### 0. Start a docker instance or a local zcashd.

This is for you to get the most speed out of your test. 
any URL to zcashd should suffice if it grants RPC access.

**You need the instance running and accessible throughout the
whole process**

### 1. Run the generation script

Using Visual Studio Code. Add this to our `launch.json` file
```json
{
            "name": "Python: Generate Advanced ReOrg tests base dataset",
            "type": "python",
            "request": "launch",
            "program": "advanced-reorg-tests/Scripts/generate_base_dataset.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "args": [
                "http://user:password@127.0.0.1:8232",
                "100"
            ]
        }
```

use python 3.9 or greater.

`python3.9 Scripts/generate_base_dataset.py "http://user:password@127.0.0.1:8232" 100`


This generation script takes around 15 seconds per transaction on Docker for mac and 2 seconds per transaction on a local zcashd. So it will take some time.


### 2. run a local python server at `/dataset`
you can do this the way you see fit. The easiest is to use python
itself

`python3 -m http.server 8000`

this is to serve lightwalletd locally

### 3. generate the blocks file
`python3 ../sfoe/Scripts/generate_test_case/get_testcase_blocks.py http://user:password@127.0.0.1:8232 base_dataset_100.txt 202 302`

this will create the "blocks file" that can be loaded straight into dwld

### 4. generate the tree states
`python3 ../sfoe/Scripts/generate_test_case/get_testcase_treestates.py  http://user:password@127.0.0.1:8232 dataset/treestates 201 303`

this will create the tree state  json files under the `dataset/treestates` folder

### 5. generate the transactions
`python3  ../sfoe/Scripts/generate_test_case/get_testcase_transactions.py http://user:password@127.0.0.1:8232 dataset/transactions 202 302`


## Syncing the dataset on a wallet

### 1. spin up lightwalletd in darkside mode.
You should actually refer to the lightwalletd documentation just in case it has
new features or arguments that you need to pass on. But we'll give out a heads up.

`./lightwalletd --log-file /dev/stdout --darkside-very-insecure  --darkside-timeout 1000 --gen-cert-very-insecure --data-dir . --no-tls-very-insecure`


### 2. spin up an http server at folder `/dataset`

you can do this the way you see fit. The easiest is to use python
itself

`python3 -m http.server 8000`

### 3. run the setup script

from folder `/dataset` run `../Scripts/setup_up_test.sh`

### 4. start the wallet

You need to start a wallet in `regtest mode`, use the "User wallet" as 
seed phrase and 202 as birthday.

If you use Zingo CLI you could start the wallet from Visual Studio Code 
with this configuration on your launch.json file


```json
{
            "type": "lldb",
            "request": "launch",
            "name": "Run Zingo Advanced ReOrg Test",
            "cargo": {
                "args": [
                    "build",
                    "--release"
                ]
            },
            "args": [
                "--seed", 
                "wrong when collect sponsor always simple control color exercise dad merry diet script attract public lucky pen pistol depend deposit salad room similar hour",
                "--birthday",
                "202",
                "--server",
                "localhost:9067",
                "--data-dir",
                "$HOME/tmp/zingo-arot",
                "--darkside-test",
                "--regtest"
            ],
            "env" : {
                "RUST_BACKTRACE": "full"
            }
        }
```
**Expected result**

The wallet should sync. In my case I was using zingo-cli and this is
the console output

```
WARNING! regtest network in use but no regtest flag recognized!
{
  "result": "success",
  "latest_block": 302,
  "total_blocks_synced": 100
}
(regtest) Block:302 (type 'help') >> balance
{
  "sapling_balance": 0,
  "verified_sapling_balance": 0,
  "spendable_sapling_balance": 0,
  "unverified_sapling_balance": 0,
  "orchard_balance": 3400000000,
  "verified_orchard_balance": 3400000000,
  "spendable_orchard_balance": 3400000000,
  "unverified_orchard_balance": 0,
  "transparent_balance": 0
}
```
## Testing scripts.

*Note: For now these is a mere description of what can be achieved with the
produced dataset*


The following sections describe the steps that need to be followed to run 
each on of the tests. There two main "roles" in these tests. The first one 
is driving the darksidewalletd server to expose the compact blockchain 
information to the wallet under test. The second one is the wallet itself 
that needs to be sync and observed to assert that the transactions, balances
and other under test are the ones expected.

### ReOrg Changes Inbound Tx Mined Height
In this test a reorg changes the mined height of an incoming transaction.
Wallet should recover from that event and show the correct balance

pre-condition: know balances before tx at received_Tx_height arrives
1. Setup w/ default dataset
2. applyStaged(received_Tx_height)
3. sync up to received_Tx_height
   * a. verify that balance is previous balance + tx amount
4. get that transaction hex encoded data
5. stage 3 empty blocks w/heights received_Tx_height to received_Tx_height + 3
6. stage tx at received_Tx_height + 3
    * a. applyheight(received_Tx_height + 1)
7. sync to received_Tx_height + 1
8. assert that reorg happened at received_Tx_height
9. verify that balance equals initial balance
10. sync up to received_Tx_height + 3
11. verify that balance equals initial balance + tx amount

### Reorg Changes Outbound Tx Index
An outbound, unconfirmed transaction in a specific block changes height in the event of a reorg

The wallet handles this change, reflects it appropriately in local storage, and funds remain spendable post confirmation.

**Pre-conditions:**
  - Wallet has spendable funds

1. Setup w/ default dataset
2. applyStaged(received_Tx_height)
3. sync up to received_Tx_height
4. create transaction
5. stage 10 empty blocks
6. submit tx at sentTxHeight
   * a. getIncomingTx
   * b. stageTransaction(sentTx, sentTxHeight)
   * c. applyheight(sentTxHeight + 1 )
7. sync to  sentTxHeight + 2
8. stage sentTx and otherTx at sentTxheight
9. applyStaged(sentTx + 2)
10. sync up to received_Tx_height + 2
11. verify that the sent tx is mined and balance is correct
12. applyStaged(sentTx + 10)
13. verify that there's no more pending transaction

### Reorg changes Incoming Transaction Index
In this case a reorg changes the index of an incoming transaction.

1. Setup w/ default dataset
2. applyStaged(received_Tx_height)
3. sync up to received_Tx_height
4. verify balance after sync
5. trigger the reorg
6. sync again (wallet should detect the reorg)
7. check that the balance matches the values of step 4


### ReOrg Expires Inbound Transaction
In this case the wallet receives a transaction and a reorg removes it 
from the chain. This can happen if the "best chain" does not contain
that transaction, and the subsequent blocks don't include it either.

1. Setup w/ default dataset with a received transaction at `received_tx_height`
2. sync up to `received_tx_height` minus some blocks.
3. capture balance
4. sync up to `received_tx_height` or higher and capture txid of the received transaction
5. trigger the reorg that removes the received transaction from the chain
6. sync to chaintip (the wallet should recover from the reorg)7
7. verify that the balance is equal to step 3 and that the txid found on step 4 
is not present anymore.


### ReOrg Changes Inbound Tx Index In Block

Steps:
1.  sync up to an incoming transaction (`incomingTxHeight + 1`)
   * 1a. save balances
2. stage 4 blocks from `incomingTxHeight - 1` with different nonce
3. stage otherTx at `incomingTxHeight`
4. stage incomingTx at `incomingTxHeight`
5. applyHeight(incomingHeight + 3)
6. sync to latest height
7. check that balances still match

### ReOrg Changes Outbound Tx MinedHeight

A Re Org occurs and changes the height of an outbound transaction

Pre-condition: Wallet has funds

Steps:
1. create fake chain
   * 1a. sync to latest height
2. send transaction to recipient address
3. getIncomingTransaction
4. stage transaction at `sentTxHeight`
5. applyHeight(sentTxHeight)
6. sync to latest height
   * 6a. verify that there's a pending transaction with a mined height of sentTxHeight
7. stage 15  blocks from `sentTxHeight`
7. a stage sent tx to `sentTxHeight + 2`
8. `applyHeight(sentTxHeight + 1)` to cause a 1 block reorg
9. sync to latest height
10. verify that there's a pending transaction with -1 mined height
11. `applyHeight(sentTxHeight + 2)`
   * 11a. sync to latest height
12. verify that there's a pending transaction with a mined height of `sentTxHeight + 2`
13. apply height(`sentTxHeight + 15`)
14. sync to latest height
15. verify that there's no pending transaction and that the tx is displayed on the sentTransactions collection


### ReOrg Changes Inbound MinedHeight

A Re Org occurs at 663195, and sweeps an Inbound Tx that appears later on the chain.
Steps:

1. reset dlwd
2. load blocks from txHeightReOrgBefore
3. applyStaged(663195)
4. sync to latest height
5. get balances
6. load blocks from dataset txHeightReOrgBefore
7. apply stage 663200
8. sync to latest height
9. verify that the balance is equal to the one before the reorg


### ReOrg Removes Incoming Tx Forever

Re Org removes incoming transaction and is never mined
Steps:
1. sync prior to incomingTxHeight - 1 to get balances there
2. sync to latest height
3. cause reorg
4. sync to latest height
5. verify that reorg Happened at reorgHeight
6. verify that balances match initial balances


### ReOrg Removes Outbound TxAnd Is Never Mined
Transaction was included in a block, and then is not included in a block after a reorg, and expires.
Steps:
1. create fake chain
1a. sync to latest height
2. send transaction to recipient address
3. getIncomingTransaction
4. stage transaction at sentTxHeight
5. applyHeight(sentTxHeight)
6. sync to latest height
6a. verify that there's a pending transaction with a mined height of sentTxHeight
7. stage 15 blocks from sentTxHeigth to cause a reorg
8. sync to latest height
9. verify that there's an expired transaction as a pending transaction
