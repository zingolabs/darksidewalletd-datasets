#!/bin/zsh


grpcurl -plaintext -d '{ "url" : "http://localhost:8000/changes-inbound-tx-mined-index/after_reorg.txt" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks

grpcurl -plaintext -d '{ "height" : 216 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged