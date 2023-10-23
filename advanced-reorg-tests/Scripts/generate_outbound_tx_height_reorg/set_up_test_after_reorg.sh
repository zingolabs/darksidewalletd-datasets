#!/bin/zsh


grpcurl -plaintext -d '{ "url" : "http://localhost:8000/changes-outbound-tx-mined-height/after_reorg.txt" }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocks

grpcurl -plaintext -d '{ "height" : 215 }' localhost:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged