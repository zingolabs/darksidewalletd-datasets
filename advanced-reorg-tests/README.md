# Advanced ReOrg Tests

This is a set of tests originated as part of integration testing of the [ECC Mobile SDKs](https://github.com/zcash/ZcashLightClientKit/blob/main/Tests/DarksideTests/AdvancedReOrgTests.swift)


## ReOrg Changes Inbound Tx Mined Height
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

## Reorg Changes Outbound Tx Index
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

## Reorg changes Incoming Transaction Index
In this case a reorg changes the index of an incoming transaction.

1. Setup w/ default dataset
2. applyStaged(received_Tx_height)
3. sync up to received_Tx_height
4. verify balance after sync
5. trigger the reorg
6. sync again (wallet should detect the reorg)
7. check that the balance matches the values of step 4


## ReOrg Expires Inbound Transaction
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


## ReOrg Changes Inbound Tx Index In Block

Steps:
1.  sync up to an incoming transaction (`incomingTxHeight + 1`)
   * 1a. save balances
2. stage 4 blocks from `incomingTxHeight - 1` with different nonce
3. stage otherTx at `incomingTxHeight`
4. stage incomingTx at `incomingTxHeight`
5. applyHeight(incomingHeight + 3)
6. sync to latest height
7. check that balances still match

## ReOrg Changes Outbound Tx MinedHeight

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


## ReOrg Changes Inbound MinedHeight

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


## ReOrg Removes Incoming Tx Forever

Re Org removes incoming transaction and is never mined
Steps:
1. sync prior to incomingTxHeight - 1 to get balances there
2. sync to latest height
3. cause reorg
4. sync to latest height
5. verify that reorg Happened at reorgHeight
6. verify that balances match initial balances


## ReOrg Removes Outbound TxAnd Is Never Mined
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