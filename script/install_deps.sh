#!/bin/bash

# the following lets you run this script from whatever folder you want without problem of relative/absolute paths
SCRIPT_HOME="$( cd "$( dirname "$0" )" && pwd )"
cd $SCRIPT_HOME/..

# main script
function enter_env(){
	workon overall-insights-extractor
}
function install_os_deps() {
	echo '---> Installing os dependencies...'
	sudo apt-get install python-dev
	sudo apt-get install python-pip
	sudo apt-get install gfortran libopenblas-dev liblapack-dev
<<<<<<< HEAD
	sudo pip install virtualenvwrapper
=======
	sudo apt-get install libffi-dev libssl-dev
	sudo apt-get install freetype*
>>>>>>> b075ff3517a371bbadf41e28ed1171aef28946d8
}

function install_matplotlib() { 
	git clone git@github.com:matplotlib/matplotlib.git
	cd matplotlib
	python setup.py install
}
 
function install_program_deps() {
	echo '---> Installing dependencies of program...'
	pip install numpy
	pip install scipy

	install_matplotlib
	
	pip install -U nltk
}

#install_os_deps 
#&& 
install_program_deps

