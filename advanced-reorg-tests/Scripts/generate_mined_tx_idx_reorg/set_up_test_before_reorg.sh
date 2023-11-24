#!/bin/zsh

# reset lightwalletd
grpcurl -plaintext -d '{ "saplingActivation" : 202, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

pushd "../../dataset"

for i in {201..222}
do
    grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json
done

popd 

grpcurl -plaintext -d '{ "url" : "http://localhost:8000/changes-inbound-tx-mined-index/before_reorg.txt" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks

grpcurl -plaintext -d '{ "height" : 203 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged

