#!/bin/bash

mdir=$1
mMassPoint=$2

cd $mdir

cmsDriver.py step2 --mc --eventcontent PREMIXRAW --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX" --datatier GEN-SIM-RAW --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v14 --procModifiers premix_stage2,siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3 --filein file:mUFO_ALP_m"$mMassPoint"_GEN-SIM.root --fileout file:mUFO_ALP_m"$mMassPoint"_SIM_DIGI-HLT.root -n -1 --no_exec

cd -
