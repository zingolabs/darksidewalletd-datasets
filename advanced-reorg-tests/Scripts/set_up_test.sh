#!/bin/zsh

# reset lightwalletd
grpcurl -plaintext -d '{ "saplingActivation" : 202, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

for i in {201..302}
do
    grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json
done

grpcurl -plaintext -d '{ "url" : "http://localhost:8000/base_dataset_100.txt" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks

grpcurl -plaintext -d '{ "height" : 302 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged


