#!/bin/bash

# the following lets you run this script from whatever folder you want without problem of relative/absolute paths
SCRIPT_HOME="$( cd "$( dirname "$0" )" && pwd )"
cd $SCRIPT_HOME/..

# main script
echo '---> Changin permission of folder'"$(pwd)"' on this machine'
chmod -R 777 ./
