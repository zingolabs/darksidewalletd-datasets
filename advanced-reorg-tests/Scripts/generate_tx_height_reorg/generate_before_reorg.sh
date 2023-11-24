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

mkdir before_reorg

pushd before_reorg

BLOCKS_DIR=$PWD
echo "BLOCKS DIR $BLOCKS_DIR"
popd

pushd "../../dataset/changes-inbound-tx-mined-height"

DATASET_DIR=$PWD
echo "DATASET DIR: $PWD"

popd


seq 202 222 | while read i; do touch before_reorg/$i.txt; done
cat "../../dataset/transactions/203/733e0764710bf9740d3c591c25ec3ebdc6799ee0ee4417d009270cc437a8be45" >> before_reorg/203.txt

pushd $GEN_BLOCKS_PATH

go run main.go --start-height 202 --blocks-dir $BLOCKS_DIR > $DATASET_DIR/before_reorg.txt

rm -rf $BLOCKS_DIR