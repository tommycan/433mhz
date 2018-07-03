#!/bin/bash
# anty  2018-06-06
# test remoter  switch

#echo "a1on[1]"
python transmitt.py a1on[1]
sleep 1s 

#echo "a1off[1]"
python transmitt.py a1off[1]
sleep 1s 

#echo "b1on[1]"
python transmitt.py b1on[1]
sleep 1s

#echo "b1off[1]"
python transmitt.py b1off[1]
sleep 1s
