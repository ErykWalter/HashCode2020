#!/bin/bash

out=$(cat $1 | ./main.py )
./checker.out $1 $out
