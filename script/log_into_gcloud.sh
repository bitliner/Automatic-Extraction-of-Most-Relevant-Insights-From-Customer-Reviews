#!/bin/bash

# the following lets you run this script from whatever folder you want without problem of relative/absolute paths

SCRIPT_HOME="$( cd "$( dirname "$0" )" && pwd )"
cd $SCRIPT_HOME/..

# main script
gcloud compute --project "nlp1-965" ssh --zone "europe-west1-c" "word2vec-model-amazone-reviews"
