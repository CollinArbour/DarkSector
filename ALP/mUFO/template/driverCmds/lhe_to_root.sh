#!/bin/bash

mdir=$1
mMassPoint=$2

cd $mdir

cmsDriver.py Configuration/Generator/python/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step GEN,SIM --nThreads 4 --era Run3 --geometry DB:Extended --beamspot Realistic25ns13p6TeVEarly2022Collision --filein file:mUFO_ALP_m"$mMassPoint"_events.root --fileout file:mUFO_ALP_m"$mMassPoint"_GEN-SIM.root -n 10000 --no_exec

cd -
