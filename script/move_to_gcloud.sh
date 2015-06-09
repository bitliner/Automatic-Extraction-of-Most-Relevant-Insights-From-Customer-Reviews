#!/bin/bash

# the following lets you run this script from whatever folder you want without problem of relative/absolute paths
SCRIPT_HOME="$( cd "$( dirname "$0" )" && pwd )"
cd $SCRIPT_HOME/..

# main script
echo "---> Moving files to remote machine on gcloud"
gcloud compute copy-files test_data.txt w_barkhof_gmail_com@word2vec-model-amazone-reviews:/home/w_barkhof_gmail_com
