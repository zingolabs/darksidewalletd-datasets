#!/bin/zsh

# reset lightwalletd
grpcurl -plaintext -d '{ "saplingActivation" : 1, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

for i in {1..1204}
do
    grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json
done


grpcurl -plaintext -d '{ "url" : "http://localhost:8000/sfoe_blocks.txt" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks

grpcurl -plaintext -d '{ "height" : 1204 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged


