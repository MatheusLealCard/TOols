#!/bin/bash

for list in $(cat $1);
do
host -t cname $list.$2 | grep "alias for";
done
