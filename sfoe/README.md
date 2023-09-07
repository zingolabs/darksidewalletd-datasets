## SECOND FLUSH OF ENTHUSIASM SCENARIO
The idea of this benchmark scenario is the following:

A user gets onboarded into ZEC at a given time (block 1)  and creates a wallet.
User forgets about it until a later time it realized it can accept a Zcash payment instead of fiat, so User intends to receive ZEC. 

**Given that user has:**
- 10 unspent note commitments 
- 100,000 blocks with two orchard actions each have passed from the onboarding moment

And will receive 2 unspent note commitments at block 100,000.

The dataset has to be 100K blocks long

**Metrics that can be derived from this benchmark:**
- Time to sync
- Time to spend onboarding funds
- Balance accuracy

### Regtest Blockchain Setup:

There is a benchmark client spend key, which is the key that represents the onboarded user's wallet.

Then there's another block population spend key, which produces outputs the users's wallet can't decrypt but will have to scan through anyway.

Original Block:    10 unspent note commitments

Filler Blocks

    * 2 orchard actions

    * 100_000 blocks

Return to Zcash:  2 unspent note commitments

### Actors on the benchmark test.

#### Miner Wallet:

*Note:* This is not actually being used because of zcashd limitations. It's not possible at the moment to restore a seed into Zcashd. The Zcashd wallet (and whatever its keys are) is used instead. We leave this for when this is actually possible.

phrase: "web element word lady flush door problem fashion various festival spin story extra spend fan truth silent skull sadness earn major quarter picture alien"

UA: `uregtest1gqnk5lxvwq7l0g5l06tm00er0f6rwhrenmczv9lfecu5j8mcj32murx7839fwcc9zs6jl6ax08zcq3kjqqag5runs62avjuv7e45ek9zngx603pzes5sezsyn36zgl94m2a3juy4jkj5f6g5gnpqdrxydh48ue0hez5wgq0xkwy9rjyrk3vmcjfmuyw97zp9rlvqxnhjs46qkq0ke33`

Role:
- Receives coinbases and distributes payments to user and generates filler outputs.

#### User wallet:
phrase: "wrong when collect sponsor always simple control color exercise dad merry diet script attract public lucky pen pistol depend deposit salad room similar hour"

seed bytes: `716a2354c5c6e0330e219f5bda06a620471da0f00338c1db3b4b05277c544a1676b6ec9af3f9405f108db4ed39c0369a4acc5cff622597d85d77dc95438ebaa4``

UA: 
`uregtest19sufy4qyv6f52773a3tklff0muzwjyv3hlqjvtp6z8spwf6xteksr5u7gmdv6h5g6wpz0flaeutxcaqqwwafffhvqetudsvfe7mtnn62yuzv77uv7azskfrqd6dqyz0zhms3yn2wjd82dqetgzddc6h0kf0t3jphenc3ts62jmcsh83ra2nj0fqeuuflq6a6asaq4fjdrzhlq5w7twd`
**Role:**
- receives funds at the beginning of the test, and then at the end, when 100 days of blocks have passed in between.

#### Filler wallet:
phrase: "nice trick fit flee all fresh jazz double renew chalk drip wheel maid nuclear favorite junior sea run acid sad virtual express topple faint"

seed bytes: `00ee85b3e3a5e6f92834abfdfef7ed3a1e552df7c005a0abbe24f3bba01e0ab4da0fe1e70a275576ec31029285b3fdca0ae2e3c97a4fa65d7e69c8e4f3867d43``

UA: 
`uregtest1fl28qdx08zgweef5ve4usg3u2fan5cgth7rnc77wkq5rm8az8rluct727p58vfm64r5zkj90aqmd9rlatqnalkh0zrmw4sy6sgaex3gnux3ahkq3lr542nlags0l2ax257clhdwkqcps2pjxnmawgzqdfpeuqtch889ml9dfmqeq0zapkgw86hzs5sfj3s3vgnt477a7x25c7yjr62j`

**Role:** gets sent all the transactions that will be filler outputs for the test.


### Elements built:

- A script that generates the scenario 
  - constructs the generate to block to the 'miner wallet' 
  - funds the user wallet with 10 orchard commitments at block `testStartHeight` 
  - generates `fillerBlockCount` filler blocks to a different wallet that can't be decrypted by user wallet. 
  - funds the user wallet at block `testStartHeight + fillerBlockCount + 1`
- Export the dataset from Regtest into darksidewalletd 
  - Get Tree States from a block range 
  - Get Transactions on every block of a given block range
  - Dump a file with the generated SFoE Test
- create a test case that exercises this test on zingo-lib

Note: the dataset should work on any other wallet (Ywallet, NH, Zashi) provided its test cases for darksidewalletd are coded.

## Topology if the SFoE test

SFoE departs from 100 "matured" coinbases at block 200. 
The test is composed of some key elements:
- `testStartHeight`: this is the height at which SFoE concretely starts. This is the first block that contains a transaction for the "user wallet".
- `fillerBlockCount` filler blocks: These are blocks that contain shielded ouputs that don't belong to the user wallet and that the wallet will have to handle anyway.
- `testEndHeight` height.

When running `generate_sfoe.py` the script will:
1. Make sure that your Zcashd regtest ready on zero blocks
2. Generate account 0 and a new address on you node (miner)
3. Generate the first 100 blocks, to have a matured coinbase that you can shield.
4. Shield the mature coinbases in 100 subsequent blocks
5. Define SFoE starting at the corresponding height (around block 202)
6. send the first z_sendmany with 10 unspent commitments for User wallet and 2 filler outputs for filler wallet
7. start generating filler blocks (1000). Each fille block has 2 transactions + the coinbase. It takes around 10 seconds for a docker Zcashd to generate a Tx. 
8. Generate a transaction with 2 unspent note commitments for user wallet (around block `start + filler_count`)
9. Generate a block for that transaction.
10. Wrap the test and inform the start, end and length of the test.

## Generating the test from scratch

### Context:

Regtest Zcashd is somewhat unstable and it's hard to create long tests with it.
After much research and attempts to create a test that comes out directly from
Regtest, it was decided that it was inpractical and time consuming and somewhat
technically impossible due to the limitations Zcashd has on note selection issues
and all.

*Known Issues:*
- `z_sendmany` and `z_shieldcoinbase` can't be parallelized to speed them up. They
would take from 1 or to seconds to 10 or more seconds depending on the hardware 
resources available on your setup. Making 2 operations and awaiting for them does
not make much difference, they are not processed concurrently. If it takes 10 seconds
to make one of these spends, making two at once, will take around 20. Plus, it might fail
due to the following issue
- "duplicate nullifier" when spending funds from the Zcashd wallet. The wallet is not 
specifically smart when selecting spendable notes. It does not do a fair job at locking
the selected notes so they are not also selected in a future or concurrent spend. 
- `main: ContextualCheckBlockHeader: block at height 1238, timestamp 1694010597 is too far ahead of median-time-past, limit is 1694010517`: this happens when creating too many blocks upfront. 

### Approach A: Creating all blocks and running entirely from Regtest
### 1. Running Zcashd regtest on docker

Follow [this article on Free2z](https://free2z.cash/pacu/zpage/running-a-zcashd-regtest-node-with-docker)


### 2. set up your folder paths to export the test

This entails setting up your persistent store for the docker instance,
and also the destination folder for the generating scripts

### 3. Launch zcashd instance in regtest (instructions on tutorial)
It is possible that you can use the docker desktop GUI as well to do
this step.

### 4. Run generate and dump script.

**Example:**

Your `rpcuser` is `usr` and your `rpcpassword` is `pwd`

Your zcashd dockerized instance is mapped to port `8232`

Run the script


`sfoe/Scripts/generate_test_case/generate_and
_dump_sfoe.py http://usr:pwd@127.0.0.1:8232 $HOME/tmp/SFoE`

### 5. [Optional] avoid recreating the whole test in zcashd when re-running the script

The script can be told to skip the generation of the Regtest blockchain, and go
straight to the "dumping" part. This is done by specifying two arguments:

`--skip-gen START_HEIGHT` tells the script to start dumping the test info from 
the given height

`--end-height END_HEIGHT` tells the script to dump *up to* `END_HEIGHT`.

Running the script without generating the blocks in regtest:

`sfoe/Scripts/generate_test_case/generate_and
_dump_sfoe.py http://usr:pwd@127.0.0.1:8232 $HOME/tmp/SFoE --skip-gen 206 --end-heigh
t 210`


### 6. Loading Into Darkside Lightwalletd

1 - run dlwd

`./lightwalletd --log-file /dev/stdout --darkside-very-insecure  --darkside-timeout 1000 --gen-cert-very-insecure --data-dir . --no-tls-very-insecure`

2 - run a local python server at `sfoe/dataset`

`python3 -m http.server 8000`

3 - run the loading script `sfoe/dataset/set_up_full_test.sh`


#### 7. Starting a Wallet that loads this test (ZingoLabs)

The test is comprised of three parts:
1. A local http server to speed loading up the data into darksidewalletd
2. A local darksidewalletd instance
3. A subject wallet that we are going to test.

Once you have completed the previous step the only thing left you need to do
is to start a wallet with the "user wallet", which is the wallet receiving the 
funds at the beginning and the end of the test.


Your `--data-dir` can be where it's suitable for you.

`--server` will point to the local lightwalletd instance. 


```
./target/release/zingo-cli \
--seed "wrong when collect sponsor always simple control color exercise dad merry diet script attract public lucky pen pistol depend deposit salad room similar hour" \
--birthday 206 \
--server localhost:9067 \
--data-dir $HOME/tmp/zingo-sfoe \
--darkside-test \
--regtest
```

### Approach B: Generating the needed materials on Regtest then run on darkside entirely


## Expected Results of the test
When you scan, the wallet should return

````JSON
{
  "result": "success"
}
````

The expected balance should be `orchard_balance` of `120000000` zatoshi
````JSON
{
  "sapling_balance": 0,
  "verified_sapling_balance": 0,
  "spendable_sapling_balance": 0,
  "unverified_sapling_balance": 0,
  "orchard_balance": 120000000,
  "verified_orchard_balance": 120000000,
  "spendable_orchard_balance": 120000000,
  "unverified_orchard_balance": 0,
  "transparent_balance": 0
}
````
