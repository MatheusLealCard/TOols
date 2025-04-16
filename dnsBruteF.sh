#!/bin/bash

for list in $(cat $1);
do
host $list.$2 | grep -v "NXDOMAIN";
done
