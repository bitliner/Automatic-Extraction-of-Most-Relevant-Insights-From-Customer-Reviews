#!/bin/bash

# the following lets you run this script from whatever folder you want without problem of relative/absolute paths
SCRIPT_HOME="$( cd "$( dirname "$0" )" && pwd )"
cd $SCRIPT_HOME/..

# main script

function install_os_deps() {
	echo '---> Installing os dependencies...'
	sudo apt-get install python-dev
	sudo apt-get install python-pip
	sudo apt-get install gfortran libopenblas-dev liblapack-dev
	sudo pip install virtualenvwrapper
}

function install_program_deps() {
	echo '---> Installing dependencies of program...'
	pip install numpy
	pip install scipy
}

#install_os_deps 
#&& 
install_program_deps

