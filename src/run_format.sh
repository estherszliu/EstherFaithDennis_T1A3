#!/bin/bash

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

# run the format
source .venv/bin/activate
pip3 install --disable-pip-version-check --quiet -r requirements.txt
autopep8 --in-place --aggressive --aggressive *.py
