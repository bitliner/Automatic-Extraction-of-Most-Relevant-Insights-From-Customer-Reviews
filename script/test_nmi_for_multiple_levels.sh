#!/usr/bin/env bash

mkdir results/$2/

for i in `seq 1 $3`; do
python source/test_nmi.py $1  models/large_training/model400.doc2vec $2 400 True $i False $4;
done