# ReOrg Changes Inbound Tx Mined Height
In this test a reorg changes the mined height of an incoming transaction.
Wallet should recover from that event and show the correct balance

**pre-condition**: know balances before tx at received_Tx_height arrives
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

## The datasets:

`dataset/changes-inbound-tx-mined-height/before_reorg.txt`:

Dataset including a transaction for the "User wallet" on block 203

`dataset/changes-inbound-tx-mined-height/after_reorg.txt`: 

Dataset including the reorg'd transaction from block 203 to block 206


## Loading the datasets and using them

### Scripts that generate this dataset
Use `advanced-reorg-tests/Scripts/generate_tx_height_reorg/generate_before_reorg.sh` to generate the "before" dataset.

Use `advanced-reorg-tests/Scripts/generate_tx_height_reorg/generate_after_reorg.sh`
to generate the "after" dataset.

### Setting up the test in lightwalletd

Lightwalletd has to be started in darkside mode and set up like `advanced-reorg-tests/Scripts/generate_tx_height_reorg/set_up_test_before_reorg.sh` does. Then the "after reorg" dataset has to be loaded like `advanced-reorg-tests/Scripts/generate_tx_height_reorg/set_up_test_after_reorg.sh` does.

### Integrating into wallets.

Basically the tests are ran by following these steps:

1. Start lightwalletd in darkside mode
2. reset the state and set up the LightDInfo  
3. set up the "before reOrg" state
4. sync the wallet.
5. set up the "after reOrg" state on lightwalletd
6. check wallet reaction. make your assertions


#### Example on how to start Zingo-CLI on Visual Studio Code

add this to your `launch.json`

``` json
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
                "/some/dir",
                "--chain",
                "regtest"
            ],
            "env" : {
                "RUST_BACKTRACE": "full"
            }
        }
```