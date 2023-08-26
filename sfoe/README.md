## SECOND FLUSH OF ENTHUSIASM SCENARIO
The idea of this benchmark scenario is the following:

A user gets onboarded into ZEC at a given time (block 1)  and creates a wallet.
User forgets about it until a later time it realized it can accept a Zcash payment instead of fiat, so User intends to receive ZEC. 

**Given that user has:**
-  10 unspent note commitments 
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


### Elements to be built:

- A script that generates the scenario ✅
  - constructs the generate to block to the 'miner wallet' 
  - funds the user wallet with 10 orchard commitments at block `testStartHeight` 
  - generates `fillerBlockCount` filler blocks to a different wallet that can't be decrypted by user wallet. 
  - funds the user wallet at block `testStartHeight + fillerBlockCount + 1`
- Export the dataset from Regtest into darksidewalletd ✅
  - Get Tree States from a block range ✅
  - Get Transactions on every block of a given block range ✅
  - Dump a file with the generated SFoE Test
- create a test case that exercises this test on zingo-lib

Note: the dataset should work on any other wallet (Ywallet, NH, Zashi) provided its test cases for darksidewalletd are coded.


### Generating the test

1. Running Zcashd regtest on docker

Follow [this article on Free2z](https://free2z.cash/pacu/zpage/running-a-zcashd-regtest-node-with-docker)


2. set up your folder paths


3. Run the generating scripts


### Topology if the SFoE test

SFoE departs from 100 "matured" coinbases at block 200. 
The test is composed of some key elements:
- `testStartHeight`: this is the height at which SFoE concretely starts. This is the first block that contains a transaction for the "user wallet".
- `fillerBlockCount` filler blocks: These are blocks that contain shielded ouputs that don't belong to the user wallet and that the wallet will have to handle anyway.
- `testEndHeight` height.