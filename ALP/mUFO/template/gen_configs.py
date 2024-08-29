#!/usr/bin/env python3

import os

## Most Important Parameters
mMass = 55


####  Script

os.makedirs('./test_template',exist_ok=True)

def convertMass(mass):
    msplit = str(mass).split('.')
    if len(msplit) == 1:
        return msplit[0]
    else:
        return f'{msplit[0]}p{msplit[1]}'

mMassPoint = convertMass(mMass)

def procMP(txt_data):
    mtxt_proc = []
    for line in txt_data:
        if '{mMassPoint}' in line:
            mtxt_proc.append(line.format(mMassPoint=mMassPoint))
        else:
            mtxt_proc.append(line)
    return mtxt_proc

##------------------
## Unpack LHE file
##------------------

with open('./crab_cfg_step1_NONE.txt','r') as fl:
    mtxt = fl.readlines()

mtxt_proc = procMP(mtxt)

os.makedirs(f'/eos/cms/store/user/carbour/mc/alp/mUFO/m{mMassPoint}',exist_ok=True)
with open('./test_template/crab_cfg_step1_NONE.py','w') as fl:
    fl.writelines(mtxt_proc)

##---------------------------
## Hadronize Event (Gen-Sim)
##---------------------------

# Need to get the prevous data base!

with open('./crab_cfg_step1.txt','r') as fl:
    mtxt = fl.readlines()

mtxt_proc = procMP(mtxt)

with open('./test_template/crab_cfg_step1.py','w') as fl:
    fl.writelines(mtxt_proc)
