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

The test uses orchard funds, it does not include sapling outputs.

```json
{
    "testStartHeight": 202,
    "testEndHeight": 302,
    "blockCount": 100,
    "userTransactions": [
        "733e0764710bf9740d3c591c25ec3ebdc6799ee0ee4417d009270cc437a8be45",
        "1f868182455684a4da98f01df55d7a28b8fbad1025e3ce28e37de4f489c42097",
        "d7c5d2ce0107486ce2f3b5a2daf175f8487fe4aaf4acd66ca97511c627614d2b",
        "b3254c73b7bc98b3881b2ca9315a0a312a66d89a934f9e962769cc5f7f41d5ce",
        "71896691f964ba0bb6c509cecc65c804754230df0f8b71ec2e3716119f17f55d",
        "2d1be3ee82408eaacddc1c833c765039919b0a747781d5100bbbb9ea1b785f88",
        "34a06af6f2930b21c7a72167a348a06f59604dce2da53e9f797032642955cf66",
        "492d21948cd9620be40a6921506a400ae8b6abb45b1cdc46ca23f6926968ec11",
        "edec272d59e6a11d5f16bbf578736e9ff7cb4bf1d7f637a4f1679d1ec1b7d732",
        "0955fe35b857001373040aa63b68f9ec8b303631c4c81c7b48126a67ef4885b7",
        "2fceea9315cc1bace10d051fdbf3f4fcdfe18552ef1197e4514b015454ead5c2",
        "107d0b9acc37421f34a727d8fddf390790c2bdf22975963b05473132d99a76a3",
        "42dee58f46fce641eb47db709549df44c37fe961aa3f80bc0598fbc5d3f6289b",
        "f4cc0ae96a8f81962742c522593e52b886c9ec579019b8ab20de8f20c00bb040",
        "bc1914f05a86f50ae7616ac27f383f20d03fbc9babbe4fcb281b50f2a676aaf0",
        "5f84b2994584d06f9b2f631beec11756c5d21d2b908eeb0c7d4238f499e886f1",
        "2bc92d9215dd4b1a8f10defc885fb2be5625b2ebc1efbf98c66e5880847ea96b",
        "e0424db27dab249b88812606f51ac39eb39e1345bdf1fc57e14c3d99aa1ce092",
        "d1ab7567d815441e61bfb6090e91e1c44955910a4ef6d16b234b56bb6f4c07ac",
        "09ac120caf4a6b6123ec5a8c3cbb3d8a6ef25cf34649fea8c001ebacc711586e",
        "12654fa918090432882ba1d61e15e2072ac7837c860522af4c49f7e9c225c30e",
        "4d2b67d79d2901a00cb4c42db1eca6bb92e55713e4fd85fe2ac6a8efaad052b4",
        "4826f86db72240341d21233799923a0f0614ed4721071ea5a83eea5efe94ee2e",
        "47db6d2877fa54960ba97edbf41401029abe399aa5140f1aaa7ca13b7ab9987e",
        "b2a36fa1ac2f5aaff557c07fd3c8d41f4dd6451de3a848bd39ab2a940bbdc064",
        "4fa4f49e8fc5cd66ebd5888569bcf06cabbe13dc0def2b92bd743c05b14078a3",
        "aeba14c1fd480f828da0d0838b157578b3928ad6d88060a57ef213941e97abbb",
        "9ac77942438f79e49968b860d1c945082665fb31a59ae2bb6a3791467fbe6864",
        "6040c1d4a94b9bc1d81eede4dfd0c227c88086ac79aac375510ace5a2202761d",
        "439665a9c32a427cea99b9c14d0160fa9f381e2a63521b436da93f0402192492",
        "487a5a8d510c2af0ec7b6c4752853af386099ab636b0bc3f329fb7250f1d19fd",
        "0e1c6a0e53b4b24dde1bc7737e4f0861f40ef408b503b653ffff4a3de80b5542",
        "d15081eb2470b7fc9eb38868778a5a47b735852c7ec861aacbb4edf37ab7ea70",
        "7b6eef82b32bf7c79dd929948567c9becddb88327ab770872419869f16126192"
    ],
    "fillerTransactions": [
        "017a83d286a11e58899af9f9bf12c6b72f4614a2df58ee5b62c30fb6b2593046",
        "6cc577daea81cb589b206b169d9509ab521dd638a9d6e903bfad84d2d4f9b31f",
        "6686656e73875c497985fd01f36bf9a84883cb366932b3b1bfeeca3e43648506",
        "ce022dcc8958a4181df3d95e09a3486d9061c2e1f2d919d980727b494ecde824",
        "d1fe6e5a463cd3a9db382911bc9a654b82f8e157d2f00938b176aac51cbc4625",
        "e37c53f81a768d1e3b362a58033600ac749acc245dc8e3891d5dacccc375b276",
        "e9600588c5613549759a79f772423519d7b29462bcbc6d44af1d485e5dc11486",
        "2a5ab19a0b1dc94de83fe7892f120194a3d0c69eadfb291901f53fcf38185341",
        "0163fda2c8aa122b3411f42bf3c21598d2d90d20c600aab9f0a3118e600127e7",
        "b04304aa71dfd7f222d2cf19e9ca380cc185e4debd3387ff52b0cbddb2df7dbc",
        "03ba00a4d50d5fa894e3cdbb65ec736b65e54a149fcde65d037b9857ba12e882",
        "0c0d1793c632d6c4cf6502e7a0b9b2cf493bc0acffa6ed5db79bf967857f1336",
        "2074800d6eb748dbb9507485f10b987e68d04b388ddd48b63639f98548b2bf3c",
        "bd68d364b19ee4a74306b41f41691952bebc5de1fce4ca06529c20aa13774ffc",
        "23d766ed17f3c80f885cf83de4532cad224e66d344d51a5b02c611010278733b",
        "3af80aabbb3744b317aa4f27ec35b9a903c30d48b7fee11dff2049da3e482679",
        "089c89714e27ac66ea179d5164d413a87cceebfada66510566abd6898757a3a5",
        "0b45a19b2792d2b7f1d79d653e6111a79b2c9362590780ad8edfc3e4fd9a54ea",
        "4eff41d1f4e782aa605033c8d216ef20af5999845f906128cb9dd30325907b5d",
        "2c9713990c011367d8743e736915f803400e7210c39c5776e48c68cf1c422bcd",
        "2c1765d5d1e917ec0a49022e8ffd8da2ce9ad4134f6a7e86eac0113cee788559",
        "5dd1b8f9f6ec0e0facfa727ece9416b7e0b26b538366707ce7be2cc48f436777",
        "314b0f313d32fbabe8058fe7db9d1c591f750ca92b54d4dec4c62e7023182106",
        "e74aae3d82dad567d937b557710d54649498c07af88f8ca1ade316d015e01c03",
        "58955be0c8e261e47eed2e20e8df84a1cbaca5f867ebcfdcccf6f53b9ed3f869",
        "b47cbcace42c722c73378d6e39558f9653dab7c65ec6f8c598e403bdf4fe552d",
        "f3c6adfede89f3bc31953868d1e6cc398727ae4ea29fe2e12614f3aaf2bc7664",
        "991bb552f766e761424d0dc5cc8d429f9416aaa36249204e561f8cec83da19c4",
        "8661fbd0ba2b084516c020a1d9b51ac42b3c2b2afe42beac2470ef066b1beae2",
        "c1c27229d3818117ed8b39cb0046ac6682deaf87bc7e090ad139f75833f7de0e",
        "52268560ed3791cd09e2f69095b98e7392b49e6579a8a93d556b8dc329997022",
        "5e9a94d7d052866db79f2e702205a08edcc177c6a9d672ba9db6b6a0fc6cd582",
        "dc4016c7080081da332416641f611815cf87b1580035190a266dab11c3835267",
        "54928eb820ce07b231dd16236f8bfe9c78da6176976e0622103e4edeb83c2c70",
        "7da62afb7b4b8411855d336ed1a814f5c2be86413d0779efde34ae9df2bdf8f7",
        "7cd6e5f8ad9311d77253baffb2d8115ff55fd676e1dfba08b93efeb938422053",
        "c29f35d3a970d867974e622ab13e08e3d67476c4e6638238cfa0106e49a2460e",
        "abb907043ef00b602e749ce183b4d8c35cece43c2d2fbd32ef3e96914ffb10ad",
        "ac6abae45677dec04b0e486cb246876fb15e187b877b2b28d914a7eb319f8c3d",
        "8c811fe8d44d3d4593d9abba0d3e869a490551eced01fcd0409168993781b9a5",
        "3deaa16aaf49a900c458d8a31486d090a9aad0e79bcd308adf946acc0e58eede",
        "1cafda3b70899d3bef151b383b8a529de8d8344a51edf4fde4e00e13fbbbc428",
        "d6a0bb4be565ea66adbfdf93790d8fdf0b4abfbc6b9a78d0382b71a102bdadf0",
        "68dac0f82d656da20e97462eb768f7bb315263fbae2f2f8dc8205ff6fe1dc75a",
        "d840d3cdabd75714c1e4d887b464181739c3337f93f0b85553f68d1a62b5b286",
        "a3e95710e303e4f84e25988563b7cc5735ae2e0e279ed1f79e53d3ca571aeb21",
        "d49491296e523275a85109bc8474693d225698f48240c69da78ddacda746116d",
        "2bfcd2c1ae93a230890004c184438ae17b75dab7f6c65181d2583f37de631cd4",
        "719f462f597ba7097e7abdf939009519419c339f3f6f60f74bb8ebab3b11eabb",
        "75c114a8392a665e6f3d90c8ea0014ff0f864265e999ab4210d242ef825510ba",
        "3b97cbf8abe28005c4a37e0656c0327acf965b3bf7e6e3b3320e7684eee70d7c",
        "d2498dd4f75c92b511db0dd1651f6d5de6c92046e40a739b1651a5f7ab1a428a",
        "423c50d006280bd52849e98ac0c6fad3b95b63a276b82fc67cd0dddd903d5a63",
        "2a6452fef1a4f59e3f83d86793cfa07621d5cb376a84722fd36021e4d32c53fb",
        "7d3f9c5a7686523b45201dcaa87ad3f1df919ff1b0b8e9d9472e72adb08314ce",
        "d854217059cdd2c932fc5a1f547e68982484f0bb2b8b281966e4d6aace9c0720",
        "9910d85ef8998d3a28059bee4398d157cf4bb72ee2adb1a5f4e2df83f4b39d36",
        "88f4c9723c38610c8a8c7e976f7ec8d2059a54f9e9dc122f421f3221c29a6e01",
        "43b12a6f884177bbb6b88a81ad93998477fcc74f3fd63f863fba0f0783e2aa6d",
        "bdce108fcc861a189481f57321f795464702f9b59c348fae481132046f432220",
        "7db87395f6ced90747603eba591aeb52d93ff40f811999f3c22a0b76edee7d19",
        "2944bb3c292911613a976afa1745de621e387398668b2bd4c09912bac39580d2",
        "dd8f120cf9f4c7793757bda5dd5a1af9f14b1e92c9ecabafd6e0879b98bac623",
        "b41e9b247e8de37c9a0d72cd611f8d996b73a452eb4b9818d6e71292ff6a5850",
        "55b4521036e28130cec6c2123fbe6f750a766388fcb808ce3db0f635efe9dd67",
        "75fc75d744002015ff069e46eaf6ef9a7c995a0b2a5dca71481427aecfd68367"
    ]
}
```


#### Folder Structure
```
dataset/
   transactions/ -> the transactions ordered by blockheight
   treestates/ -> the tree states of the dataset
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


### 2. run a local python server at `sfoe/dataset`
you can do this the way you see fit. The easiest is to use python
itself

`python3 -m http.server 8000`

this is to serve lightwalletd locally

### 3. generate the blocks file
`python3.9 ../sfoe/Scripts/generate_test_case/get_testcase_blocks.py http://user:password@127.0.0.1:8232 base_dataset_100.txt 202 302`

this will create the "blocks file" that can be loaded straight into dwld

### 4. generate the tree states
` python3.9 ../sfoe/Scripts/generate_test_case/get_testcase_treestates.py  http://user:password@127.0.0.1:8232 dataset/treestates 201 303`

this will create the tree state  json files under the `dataset/treestates` folder

### 5. generate the transactions
`python3.9  ../sfoe/Scripts/generate_test_case/get_testcase_transactions.py http://user:password@127.0.0.1:8232 dataset/transactions 202 302``


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
5. stage 5 empty blocks w/heights received_Tx_height to received_Tx_height + 3
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
