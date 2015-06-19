#!/usr/bin/env bash

mkdir results/$1/

for i in `seq 1 $2`; do
python source/test.py data/constructed-review-data/constructed-sentences-20 models/large_training/model400.doc2vec $1 400 True $i False $3;
done