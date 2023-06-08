#!/bin/bash

if [ $# != 1 ]
then
    echo "Arguments: [filename]"
    exit -1
fi

filename=$1

sort -n -k 1 -o $filename $filename