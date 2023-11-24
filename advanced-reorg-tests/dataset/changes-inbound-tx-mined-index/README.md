# Reorg changes Incoming Transaction Index
In this case a reorg changes the index of an incoming transaction.

1. Setup w/ default dataset
2. applyStaged(received_Tx_height)
3. sync up to received_Tx_height
4. verify balance after sync
5. trigger the reorg
6. sync again (wallet should detect the reorg)
7. check that the balance matches the values of step 4

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