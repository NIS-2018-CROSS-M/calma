#!/bin/bash

ONMTTEST=~/OpenNMT-py/translate.py
                                           
LAN=SOMELAN

echo $LAN
python3 $ONMTTEST -model models/$LAN-model_step_10000.pt -src opennmtdata/$LAN-src-test.txt -output results/$LAN-src-test.txt.out -replace_unk -verbose  -gpu 0 -n_best 10 -beam 10 > results/$LAN-src-test.txt.nbest.out

