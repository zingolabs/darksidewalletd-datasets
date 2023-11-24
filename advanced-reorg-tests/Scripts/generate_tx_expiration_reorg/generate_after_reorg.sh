#!/bin/sh

# In this test a reorg changes the mined height of an incoming transaction.
# Wallet should recover from that event and show the correct balance

function usage() {
    echo "USAGE: $0 GEN_BLOCKS_PATH";
}

GEN_BLOCKS_PATH=$1;


if [ -f "$GEN_BLOCKS_PATH/main.go" ]; then
    echo "GEN_BLOCKS_PATH exists at $GEN_BLOCKS_PATH";
else 
    echo "GEN_BLOCKS_PATH does not exist.";

    usage;
    exit 1;
fi

mkdir after_reorg

pushd after_reorg

BLOCKS_DIR=$PWD
echo "BLOCKS DIR $BLOCKS_DIR"
popd

pushd "../../dataset/expires-inbound-transaction"

DATASET_DIR=$PWD
echo "DATASET DIR: $PWD"

popd

# This is fine. We need all empty blocks 
seq 202 222 | while read i; do touch after_reorg/$i.txt; done

pushd $GEN_BLOCKS_PATH

go run main.go --start-height 202 --blocks-dir $BLOCKS_DIR > $DATASET_DIR/after_reorg.txt

rm -rf $BLOCKS_DIR