#!/bin/bash

mdir=$1
mMassPoint=$2

cd $mdir

cmsDriver.py step3 --mc --eventcontent AODSIM --datatier AODSIM --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 4 --geometry DB:Extended --era Run3 --procModifiers siPixelQualityRawToDigi --filein file:mUFO_ALP_m"$mMassPoint"_SIM_DIGI-HLT.root --fileout file:mUFO_ALP_m"$mMassPoint"_AOD.root -n -1 --no_exec

cd -
