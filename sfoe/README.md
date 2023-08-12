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

Role:
- Receives coinbases and distributes payments to user and generates filler outputs.

#### User wallet:
phrase: "wrong when collect sponsor always simple control color exercise dad merry diet script attract public lucky pen pistol depend deposit salad room similar hour"

**Role:**
- receives funds at the beginning of the test, and then at the end, when 100 days of blocks have passed in between.

### Elements to be built:

- A script that generates the scenario
  - constructs the generate to block to the 'miner wallet'
  - funds the user wallet with 10 orchard commitments at block 1
  - generates filler blocks to a different wallet that can't be decrypted by user wallet.
  - funds the user wallet at block 100K
- Export the dataset from Regtest into darksidewalletd
- create a test case that exercises this test on zingo-lib

Note: the dataset should work on any other wallet (Ywallet, NH, Zashi) provided its test cases for darksidewalletd are coded.

