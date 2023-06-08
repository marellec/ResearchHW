#!/bin/bash

if [ $# != 2 ]
then
    echo "Arguments: [filename] [num_records]"
    exit -1
fi

filename=$1
num_records=$2


i1="$filename.i1"
i2="$filename.i2"
s1="$filename.s1"

# output file
:> $filename

# random 32-bit integers
gshuf -i 0-4294967296 -n $num_records > $i2
gshuf -i 0-4294967296 -n $num_records > $i1

# random 100-byte ascii strs
base64 -i /dev/urandom | fold -w 100 | head -n $num_records > $s1

# <int1> <int> <str>
paste $i1 $i2 $s1 > $filename

rm $i1
rm $i2
rm $s1