#!/usr/bin/env python3

import os

_steps=['step1_NONE','step1']

def convertMass(mass):
    msplit = str(mass).split('.')
    if len(msplit) == 1:
        return msplit[0]
    else:
        return f'{msplit[0]}p{msplit[1]}'

def loadStepTemplate(step):
    flnm = f'./templates/crab_cfg_{step}.txt'
    with open(flnm,'r') as fl:
        mtxt = fl.readlines()
    return mtxt

def procMP(mMassPoint,txt_data):
    mtxt_proc = []
    for line in txt_data:
        if '{mMassPoint}' in line:
            mtxt_proc.append(line.format(mMassPoint=mMassPoint))
        else:
            mtxt_proc.append(line)
    return mtxt_proc

def store(step,data):
    with open(f'./test_out/crab_cfg_{step}.py','w') as fl:
        fl.writelines(data)



if __name__ == '__main__':

    ## Most Important Parameters
    mMass = 52.5
    mMassPoint = convertMass(mMass)


    mtxt = loadStepTemplate(_steps[0])
    mtxt_proc = procMP(mMassPoint,mtxt)
    store(_steps[0],mtxt_proc)

