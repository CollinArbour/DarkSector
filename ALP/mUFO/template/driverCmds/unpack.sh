#!/bin/bash

mdir=$1
mMassPoint=$2

cd $mdir

cmsDriver.py step1 --filein file:mUFO_ALP_m"$mMassPoint"_events.lhe --fileout file:mUFO_ALP_m"$mMassPoint"_events.root --mc --eventcontent LHE --datatier LHE --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step NONE --era Run3 -n 10000 --no_exec

cd -
