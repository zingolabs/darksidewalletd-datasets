# Darksidewalletd Datasets

## What is this for?
This is a repo Zingo Labs is publishing to contribute a set of reference datasets 
for the whole Zcash wallet developer community. 

Our goal is to achieve a testing baseline for our wallet that can be used as 
reference for all Zcash light wallets of the ecosystem

### What is Darksidewalletd?
Zcash light clients (wallets) use [lightwalletd](https://github.com/zcash/lightwalletd) to connect to the blockchain. Lightwalletd is a Go implementation of [ZIP-307](https://zips.z.cash/zip-0307). Light
clients connecting to a lightwalletd server assume that it's an honest but curious actor. That model
allow developers to create a synthetic blockchain to emulate different sync cases for wallets. That's
what Darksidewalletd is. You can learn about darksidewalletd [here](https://github.com/zcash/lightwalletd/blob/master/docs/darksidewalletd.md)

This is Zingo Labs' take on darksidewalletd testing. We encourage all wallet teams to contribute,
maintain and expand these datasets.

If you are looking for older dataset you should refer to [this other repo](https://github.com/pacu/darksidewalletd-test-data) that has v4 transactions and mainnet blocks. 

## Directory structure.

Each directory is a test bundle. Each folder has all the necessary pieces to reproduce the dataset
and make the best of it. Each Folder should have a README.md file with the necessary instructions 
or description sections (but not limited to): 
- What it the dataset for
- Testing scenarios it provides
- Any set-up scripts
- testing scripts with outcomes expected for success (or failures) under test

