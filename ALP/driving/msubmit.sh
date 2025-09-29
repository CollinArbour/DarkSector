#!/bin/bash

mMassPoint=$1

cd ../m$mMassPoint

crab submit -c crab_cfg_step1_NONE.py

cd -
