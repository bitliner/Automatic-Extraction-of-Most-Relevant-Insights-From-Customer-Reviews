#!/usr/bin/env bash

# $1 = data
# $2 = model
# $3 = name/method of linkage
# $4 = level


for i in `seq 1 $4`; do
python source/test_dendrogram.py $1 $2 $3 400 $i 0 $3 0 0 20;
done

for i in `seq 1 $4`; do
python source/test_nmi.py $1 $2 $3 400 1 $i 0 $3;
done

