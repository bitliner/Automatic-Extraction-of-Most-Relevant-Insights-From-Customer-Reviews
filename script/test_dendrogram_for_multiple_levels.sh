#!/usr/bin/env bash

# 1 = data
# 2 = output folder
# 3 = levels

mkdir results/$2/

for i in `seq 1 $3`; do
python source/test_dendrogram.py $1 models/large_training/model400.doc2vec $2 400 $i 0 $2 1 20;
done