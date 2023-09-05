#!/bin/zsh

# this test is laying the ground for creating the 100K but I need to take babysteps since lightwalletd since pretty unstable for some reason.
echo "grpcurl -plaintext -d '{ "saplingActivation" : 1, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset"
# reset lightwalletd
grpcurl -plaintext -d '{ "saplingActivation" : 1, "branchID" : "2bb40e60", "chainName" : "regtest"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

for i in {1..1203}
do
    echo "grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json"

    grpcurl -plaintext -d @ localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState < treestates/$i.json
done

for i in {1204..100003}
do
    # fake a tree
    echo "fake TreeState for height $i"
    grpcurl -plaintext -d "{ \"network\": \"regtest\", \"height\": \"$i\", \"hash\": \"0a1cd1eb4a5cbaa77c148cd25f328037e35361ea238b388e589c78b0e128851e\",  \"time\": 1693145091,  \"saplingTree\": \"000000\",  \"orchardTree\": \"0117fbeab74845d1bd29a48188b01899eec59fb39c6f62bd878c5f776cb622b02a001f000001bcd2386e5fa6c64795384896775ee135493fce28e5d39aae7b49ff78cb303301014a6597ad0ed0853900685983df257435fc0488e300eb68120135f1610d0f0721000000000000000000000000000000000000000000000000000000\"}" localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState
done

echo "fake TreeState for height 100004"
grpcurl -plaintext -d "{ \"network\": \"regtest\", \"height\": \"100004\", \"hash\": \"0a1cd1eb4a5cbaa77c148cd25f328037e35361ea238b388e589c78b0e128851e\",  \"time\": 1693145091,  \"saplingTree\": \"000000\",  \"orchardTree\": \"0199aa1a2d9d6904a30373bfef0704457a27dad086ad3fe4f4007ec5c2a80c39200117fbeab74845d1bd29a48188b01899eec59fb39c6f62bd878c5f776cb622b02a1f0001da3de1cab4d98239aecefed49397ba5a91c82fcc2138471d3186c05a85073e0a00000101baee5e0a7902397807a67f57ef4969da91b4229910458288ace26db52deb0e0000000000000000000000000000000000000000000000000000\"}" localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState

echo "load 1204 blocks from regtest"

grpcurl -plaintext -d '{ "url" : "http://localhost:8000/sfoe_blocks.txt"  }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks

echo "create 98800 synthetic blocks from 1204 onwards" 
grpcurl -plaintext -d '{ "height" : 1204, "nonce" : 0, "count": 98800 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocksCreate

for i in {1204..100003}
do
    echo "Stage Filler Transactions at height $i"
    grpcurl -plaintext -d "{ \"height\" : $i, \"url\" : \"http://localhost:8000/transactions/400/2291eec04f559fe5ea995996c676d8c1ccd999f1aaf64a3d321fc00b220d4b0f\" }" localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions
    grpcurl -plaintext -d "{ \"height\" : $i, \"url\" : \"http://localhost:8000/transactions/400/c03cc9b01a7f0df7ecac96d62fd6e189ff4a98acaf9617a53e4ad15010cbe40b\" }" localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions
    grpcurl -plaintext -d "{ \"height\" : $i, \"url\" : \"http://localhost:8000/transactions/400/ec287eec2d3db38dcdd3056eeb9726e844e82ec7ee8f8737c043562b7e5c41a8\" }" localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions
done

grpcurl -plaintext -d '{ "height" : 100003, "url" : "http://localhost:8000/transactions/1204/9b034bb694fbc37f4158c31d563065de8d8c8d54647302b3b60a42c865c6ad94" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions
grpcurl -plaintext -d '{ "height" : 100003, "url" : "http://localhost:8000/transactions/1204/546c17867f0593040b1d285f47230382d86eb5ce271b0ec1b35810d71ffcd958" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageTransactions

# fake a tree
grpcurl -plaintext -d '{ "network": "regtest", "height": "100003", "hash": "0a1cd1eb4a5cbaa77c148cd25f328037e35361ea238b388e589c78b0e128851e",  "time": 1693145091,  "saplingTree": "000000",  "orchardTree": "014387f36acef73d2b8ca5d779c60951b7ce93706d1164c74f8d1c0a38f921a917019c8e1eee64ee7b076284b3028fa0e3f60d091535f409b0c7724d9c08e672651f1f01a789fccf27a61b3885b99528e772399d7a2faf11c577865855fdb7e21ef56f360000000177b33c7e3ca6727548943f553e1714758608c668df92b922b5833552a55bf9010000000000000000000000000000000000000000000000000000"}' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/AddTreeState

grpcurl -plaintext -d '{ "height" : 100003 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged

