#!/usr/bin/env bash

# $1 = data
# $2 = model
# $3 = output folder
# $4 = levels

for i in `seq 1 $4`; do
python source/test_dendrogram.py $1 $2 $3 400 $i 0 $3 0 1 20;
done