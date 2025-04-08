#!/bin/bash

mdir=$1
mMassPoint=$2

cd $mdir

cmsDriver.py step4 --mc --eventcontent MINIAODSIM --datatier MINIAODSIM --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step PAT --nThreads 4 --geometry DB:Extended --era Run3 --filein file:mUFO_ALP_m"$mMassPoint"_AOD.root --fileout file:mUFO_ALP_m"$mMassPoint"_MINIAOD.root -n 10000 --no_exec

cd -
