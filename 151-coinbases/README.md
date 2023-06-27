# 151 blocks of coinbases

## What is this?

This is a darksidewalletd dataset composed of 151 blocks of 1 transparent coinbase to the legacy t-address of zcashd and 150 shielded coinbases to sapling address.

## Folder and files
`blocks` contains all the raw blocks from the regtest zcashd each one on its own file. Not needed for darksidewalletd, but for your convenience.
`Scripts` contains the Python sacrileges that can't really be called scripts that generated this dataset
`transactions` all the raw transactions in hex-enconded strings named by their Tx IDs. one per txt file
`treestates` the tree state json files that are needed to spend these notes
`UTXOs` the UTXOs present in the chain
`zcashd-data` the `regtest` folder of zcashd for reproducibility and correction of this dataset in time
`blocks.txt` the blocks in `DarksideBlocksURL` format
`list_of_block_hashes.txt` contains just that for informational purposes
`list_of_transaction_ids.txt` contains just that for informational purposes
`zcashd_backup.txt` the backup file of zcashd extracted with `zcashd-wallet-tool`


## How to test this out

1. build `zingo-cli`
2. launch darksidewalletd [see README](../README.md)
3. run ` ./target/release/zingo-cli --seed "web element word lady flush door problem fashion various festival spin story extra spend fan truth silent skull sadness earn major quarter picture alien" --birthday 1 --server localhost:9067 --chain regtest --data-dir ~/tmp/zingo-testB`


**Expected Result**

````
WARNING! regtest network in use but no regtest flag recognized!
{
  "result": "success",
  "latest_block": 151,
  "total_blocks_synced": 51
}
(regtest) Block:151 (type 'help') >> balance
{
  "sapling_balance": 93750000000,
  "verified_sapling_balance": 93750000000,
  "spendable_sapling_balance": 93750000000,
  "unverified_sapling_balance": 0,
  "orchard_balance": 0,
  "verified_orchard_balance": 0,
  "spendable_orchard_balance": 0,
  "unverified_orchard_balance": 0,
  "transparent_balance": 0
}
````


