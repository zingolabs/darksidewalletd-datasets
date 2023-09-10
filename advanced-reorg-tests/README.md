# Advanced ReOrg Tests

This is a set of tests originated as part of integration testing of the [ECC Mobile SDKs](https://github.com/zcash/ZcashLightClientKit/blob/main/Tests/DarksideTests/AdvancedReOrgTests.swift)

## Testing scripts.

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
        "ae9a2b82ce615f9baf6a0a46f6e426dc7ac857d4d829ac429467cd6d681baf02",
        "815d8ade287773768af574753fb83a8e6d7ca49e71c7c6ac6c76e2b29fda7f35",
        "c6a6a0356724c17b8cca554d555d9da3a891adbf8dcda3389b00392fc5998c69",
        "48e26429604a45b5d5518c3e400710386126cfefe109a583a623fa7e68fe363e",
        "4c81d2d187c057024c7120ff5fc07b526a53a6b4308a1bf80862c9aac1b865b4",
        "2e39a356d02b644e4c74d7ac052759e521af91831883af9178ac4df09c3fd3e6",
        "491db7ce06e78659a70cf411f70f8d14622e635c8122cca4094e34d6ab99e8bf",
        "c00d9086f0db51f563a0c5cf9c9bf001bbcf6117f389662b0d0c223169972ae3",
        "b71d0da97d8ae8f2946bbfc1adfa0dc6c109c7b352ef73711f18c2dba7588500",
        "367c1d4d250f453e52b6b634bc7d816758f2437aff1d7c90fce13dc35dc1d867",
        "64c07983b144eb0f3e8379d0e816c70f32af4ab060be5c956f2801c04e9473f7",
        "bc036814477d97f592031d141ec0fc7eaefc2e2e5a7e56bc985ec0b20dd1eca7",
        "7bc4aa073d5dfca303b280df5926a52a9a36d8ac64f59df75ae1d9f3e8ee5b0f",
        "cf717da9a5b06bc544b7d7443d8461917bcdcf4b9884159c4df5b1a3d69b8f53",
        "e7901980f188391038e125fc11c0838e44edd4ccb90c377dabeb30053d0f59cd",
        "200e01d73543fdf6cf227c51dd82de5becc2d2622167c1dd2379f0ec2cabb92c",
        "e561d0b1911068345a0d04f78420de9bfa9499ee99a9f71c2719c08aee75d0c6",
        "a6f0aec50d01145d236cb1f68210f6c848bb8c6c46d3b65d78564bbf7d9cc906",
        "a44739c253831e6945943bd2d701666235ebafeb341a9683ff4f9defa1db9d90",
        "8ec9e9d235f47e4eb6e7814c0bc3a22613616444d336b87d73470be1da3840bb",
        "09d00f208acc51471647e04f971620df907aa4e59866521624c4d03198b7bf2c",
        "3349587b3dd09a8f67738578ac28925fea39527f8b9cfe22f3b4be0d16197488",
        "5f45513c4180b95d7ad7271fc485d5f0a322eb24e8a3352abef76a432a8f1cb8",
        "d5f1097b032daafc5ebf0c70f41e977e6c6eed992d826bc80f889401f8a4edb4",
        "4e60a2f78073c3708ac3de63e0d4592e4b604d39ed124cf631faf61179f68225",
        "e6cfdce1798ddebca8fe16bdeb27d5f45c760ebc0010d5dc9fc9db9f2e8ae0d7",
        "109e1ed7c05d129b09b90a2dc12aae626ed999c5de652a04a2807e3cf17d6b49",
        "005e028a5f6ef5b2a2e2df468d55e1a03d21cab41660fe0cee951178fbed91d1",
        "560ac2471fd4aa7c7dc60426a3fe8c54d3f03acfe7ac38f7b3893664d6d1b3c6",
        "f45bfbcfaa6c7a3d6d26ebd108c9d71c0f562a5ce9c29b22070edde8c1b546ef",
        "b3c633fa9d1e4d12a6cdea117d36608a381552a10296a87ad2b7499fd2e9edb5",
        "1d7b170fcdb8571e001c8904860cef1d0c2529c3dc5872ec93a7a0b0a1c2cb21",
        "19c24601b32d825b7c65376b578badfc7e71a2e7b2b78ae0907a9f3fee939d11",
        "762d10250f551115e2acb86d75b11334bb4bb8592741b8059c42319d53daf64e"
    ],
    "fillerTransactions": [
        "ae9a2b82ce615f9baf6a0a46f6e426dc7ac857d4d829ac429467cd6d681baf02",
        "815d8ade287773768af574753fb83a8e6d7ca49e71c7c6ac6c76e2b29fda7f35",
        "c6a6a0356724c17b8cca554d555d9da3a891adbf8dcda3389b00392fc5998c69",
        "48e26429604a45b5d5518c3e400710386126cfefe109a583a623fa7e68fe363e",
        "4c81d2d187c057024c7120ff5fc07b526a53a6b4308a1bf80862c9aac1b865b4",
        "2e39a356d02b644e4c74d7ac052759e521af91831883af9178ac4df09c3fd3e6",
        "491db7ce06e78659a70cf411f70f8d14622e635c8122cca4094e34d6ab99e8bf",
        "c00d9086f0db51f563a0c5cf9c9bf001bbcf6117f389662b0d0c223169972ae3",
        "b71d0da97d8ae8f2946bbfc1adfa0dc6c109c7b352ef73711f18c2dba7588500",
        "367c1d4d250f453e52b6b634bc7d816758f2437aff1d7c90fce13dc35dc1d867",
        "64c07983b144eb0f3e8379d0e816c70f32af4ab060be5c956f2801c04e9473f7",
        "bc036814477d97f592031d141ec0fc7eaefc2e2e5a7e56bc985ec0b20dd1eca7",
        "7bc4aa073d5dfca303b280df5926a52a9a36d8ac64f59df75ae1d9f3e8ee5b0f",
        "cf717da9a5b06bc544b7d7443d8461917bcdcf4b9884159c4df5b1a3d69b8f53",
        "e7901980f188391038e125fc11c0838e44edd4ccb90c377dabeb30053d0f59cd",
        "200e01d73543fdf6cf227c51dd82de5becc2d2622167c1dd2379f0ec2cabb92c",
        "e561d0b1911068345a0d04f78420de9bfa9499ee99a9f71c2719c08aee75d0c6",
        "a6f0aec50d01145d236cb1f68210f6c848bb8c6c46d3b65d78564bbf7d9cc906",
        "a44739c253831e6945943bd2d701666235ebafeb341a9683ff4f9defa1db9d90",
        "8ec9e9d235f47e4eb6e7814c0bc3a22613616444d336b87d73470be1da3840bb",
        "09d00f208acc51471647e04f971620df907aa4e59866521624c4d03198b7bf2c",
        "3349587b3dd09a8f67738578ac28925fea39527f8b9cfe22f3b4be0d16197488",
        "5f45513c4180b95d7ad7271fc485d5f0a322eb24e8a3352abef76a432a8f1cb8",
        "d5f1097b032daafc5ebf0c70f41e977e6c6eed992d826bc80f889401f8a4edb4",
        "4e60a2f78073c3708ac3de63e0d4592e4b604d39ed124cf631faf61179f68225",
        "e6cfdce1798ddebca8fe16bdeb27d5f45c760ebc0010d5dc9fc9db9f2e8ae0d7",
        "109e1ed7c05d129b09b90a2dc12aae626ed999c5de652a04a2807e3cf17d6b49",
        "005e028a5f6ef5b2a2e2df468d55e1a03d21cab41660fe0cee951178fbed91d1",
        "560ac2471fd4aa7c7dc60426a3fe8c54d3f03acfe7ac38f7b3893664d6d1b3c6",
        "f45bfbcfaa6c7a3d6d26ebd108c9d71c0f562a5ce9c29b22070edde8c1b546ef",
        "b3c633fa9d1e4d12a6cdea117d36608a381552a10296a87ad2b7499fd2e9edb5",
        "1d7b170fcdb8571e001c8904860cef1d0c2529c3dc5872ec93a7a0b0a1c2cb21",
        "19c24601b32d825b7c65376b578badfc7e71a2e7b2b78ae0907a9f3fee939d11",
        "762d10250f551115e2acb86d75b11334bb4bb8592741b8059c42319d53daf64e"
    ]
}
```


#### Folder Structure
```
dataset/
   transactions/ -> the transactions ordered by blockheight
   treestates/ -> the tree states of the dataset
```



```