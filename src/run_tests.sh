#!/bin/bash

verbose=$1

# check if python is installed
if [[ ! "$(python3 -V)" =~ "Python 3" ]]
then
    echo ""
    echo "[ERROR] Python 3 is not installed"
    echo ""

    exit
fi

# check if the venv already exists
if [ ! -d ".venv" ]
then
    echo "[INFO] Creating new virtual environment"
    python3 -m venv .venv
fi

# run the tests
source .venv/bin/activate
pip3 install --disable-pip-version-check --quiet -r requirements.txt

if [ $verbose = "-v" ] 
then
    python3 test_create_feature.py
    python3 test_search_feature.py
else
    python3 test_create_feature.py -b
    python3 test_search_feature.py -b
fi
