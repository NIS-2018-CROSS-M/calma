#!/bin/bash

ONMTTRAIN=~/OpenNMT-py/train.py
                                           
LAN=SOMELAN

echo $LAN
python3 $ONMTTRAIN -data opennmtdata/$LAN -train_steps 10000 -valid_steps 1000 -save_model models/$LAN-model -world_size 1 -gpu_ranks 0 1 -encoder_type brnn

