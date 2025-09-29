#!/bin/bash

mdir=$1
mMassPoint=$2

cd $mdir

cmsDriver.py step2 --mc --eventcontent RAWSIM --datatier GEN-SIM-DIGI --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step DIGI,L1,DIGI2RAW,HLT:2022v14 --procModifiers siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --era Run3 --filein file:mUFO_ALP_m"$mMassPoint"_GEN-SIM.root --fileout file:mUFO_ALP_m"$mMassPoint"_SIM_DIGI-HLT.root -n 500000 --no_exec

cd -
