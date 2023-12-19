#!/bin/bash

verbose=$1

if [ $verbose = "-v" ] 
then
    python3 test_create_feature.py
    python3 test_search_feature.py
else
    python3 test_create_feature.py -b
    python3 test_search_feature.py -b
fi
