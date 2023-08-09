#!/bin/zsh

# reset lightwalletd
grpcurl -plaintext -d '{ "saplingActivation" : 1, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

for i in {1..151}
do
    grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json
done


grpcurl -plaintext -d '{ "network": "regtest", "height": "99", "hash": "0a1cd1eb4a5cbaa77c148cd25f328037e35361ea238b388e589c78b0e128851e",  "time": 1687198326,  "saplingTree": "01a62b2061ba149440fc226ed047831b3bc85661e45d5e39e7876cff139ae0c71d01e481c619ca10a5bd314dc3b1bf56b0c01ff93a00ac98c45edeb8ee2202c487140600000000019ffdf2b552fdc5b56273f36ab90098561d1767896cd362067001ab7810bc492801ad7100cdd24579ec2ad675a3a38718cae69ab08293e30d1f22440e601715bf0b",  "orchardTree": "000000"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState

grpcurl -plaintext -d '{ "url" : "https://raw.githubusercontent.com/pacu/darksidewalletd-test-data/151-coinbases/151-coinbases/blocks.txt" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks

grpcurl -plaintext -d '{ "height" : 151 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged


