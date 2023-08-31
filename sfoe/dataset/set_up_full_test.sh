#!/bin/zsh

# this test is laying the ground for creating the 100K but I need to take babysteps since lightwalletd since pretty unstable for some reason.
echo "grpcurl -plaintext -d '{ "saplingActivation" : 206, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset"
# reset lightwalletd
grpcurl -plaintext -d '{ "saplingActivation" : 206, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

for i in {205..206}
do
    echo "grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json"

    grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json
done


grpcurl -plaintext -d '{ "url" : "http://localhost:8000/block_206.txt"  }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks
grpcurl -plaintext -d '{ "height" : 206 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged
grpcurl -plaintext -d '{ "height" : 207, "nonce" : 0, "count": 1002 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocksCreate

for i in {207..1207}
do
    grpcurl -plaintext -d "{ \"height\" : $i, \"url\" : \"http://localhost:8000/transactions/207/47dfb3ee4d00d3e9672fe6d0739a646dc8b602002699cf3af219ede09ec49a41\" }" localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions
    grpcurl -plaintext -d "{ \"height\" : $i, \"url\" : \"http://localhost:8000/transactions/207/f1bbc504b97e0f548b870d90cf7d7ef144b2b6640164bca2c56894b4a830fc10\" }" localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions
done

grpcurl -plaintext -d '{ "height" : 1208, "url" : "http://localhost:8000/transactions/210/6bb91d438eebcb563316dc061e46ed167ba6c81ce1132313ca9ed7735caa3d1a" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions
grpcurl -plaintext -d '{ "height" : 1208, "url" : "http://localhost:8000/transactions/210/671b54e577509e98d677e8f90d6864fcfcdefd1200b8c9d3a036ce350763408a" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions

# fake a tree
grpcurl -plaintext -d '{ "network": "regtest", "height": "1208", "hash": "0a1cd1eb4a5cbaa77c148cd25f328037e35361ea238b388e589c78b0e128851e",  "time": 1693145091,  "saplingTree": "000000",  "orchardTree": "014387f36acef73d2b8ca5d779c60951b7ce93706d1164c74f8d1c0a38f921a917019c8e1eee64ee7b076284b3028fa0e3f60d091535f409b0c7724d9c08e672651f1f01a789fccf27a61b3885b99528e772399d7a2faf11c577865855fdb7e21ef56f360000000177b33c7e3ca6727548943f553e1714758608c668df92b922b5833552a55bf9010000000000000000000000000000000000000000000000000000"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState

grpcurl -plaintext -d '{ "height" : 1208 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged

