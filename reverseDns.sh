#!/bin/bash

for range in $(seq $1 $2);
do
host $3.$range | cut -d " " -f5 |grep -v "eu"
done
