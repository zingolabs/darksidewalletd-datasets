#!/bin/zsh

# reset lightwalletd
grpcurl -plaintext -d '{ "saplingActivation" : 206, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

for i in {205..210}
do
    grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json
done


grpcurl -plaintext -d '{ "url" : "https://raw.githubusercontent.com/zingolabs/darksidewalletd-datasets/micro_test_gen_script/sfoe/dataset/sfoe_blocks.txt" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks

grpcurl -plaintext -d '{ "height" : 210 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged


