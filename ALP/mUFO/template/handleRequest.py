#!/usr/bin/env python3

import os

_steps=['step1_NONE.py',\
        'Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff_py_GEN_SIM.py',\
        'step2_DIGI_DATAMIX_L1_DIGI2RAW_HLT.py',\
        'step3_RAW2DIGI_L1Reco_RECO_RECOSIM.py',\
        'step4_PAT.py']

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

def procMP(mMassPoint,txt_data,mPrevDB=''):
    mtxt_proc = []
    if mPrevDB:
        mPrevDB = f'\'{mPrevDB}\''
    for line in txt_data:
        if '{mMassPoint}' in line:
            mtxt_proc.append(line.format(mMassPoint=mMassPoint))
        elif '{mPrevDB}' in line:
            mtxt_proc.append(line.format(mPrevDB=mPrevDB))
        else:
            mtxt_proc.append(line)
    return mtxt_proc

def store(mass,step,data):
    with open(f'../m{mass}/crab_cfg_{step}.py','w') as fl:
        fl.writelines(data)

def execute(mass,step):
    return_to = os.getcwd()
    os.chdir(f'../m{mass}/')
    os.system(f'crab submit -c crab_cfg_{step}.py')
    os.chdir(return_to)

def runCMSDriver(mass,step):
    if step == 'step1_NONE':
        os.system(f'./driverCmds/unpack.sh ../m{mass}/ {mass}')
    elif step == 'step1':
        os.system(f'./driverCmds/lhe_to_root.sh ../m{mass}/ {mass}')
    elif step == 'step2':
        os.system(f'./driverCmds/digi_hlt.sh ../m{mass}/ {mass}')
    elif step == 'step3':
        os.system(f'./driverCmds/reco.sh ../m{mass}/ {mass}')
    elif step == 'step4':
        os.system(f'./driverCmds/miniAOD.sh ../m{mass}/ {mass}')

def findDB(mass,step):
    if step == 'step1':
        os.system(f'crab status -d ../m{mass}/crab_mUFO_ALP_m{mass}_step0 >> ./temp_status.txt')
    elif step == 'step2':
        os.system(f'crab status -d ../m{mass}/crab_projects/crab_mUFO_ALP_m{mass}_step1 >> ./temp_status.txt')
    elif step == 'step3':
        os.system(f'crab status -d ../m{mass}/crab_projects/crab_mUFO_ALP_m{mass}_step2 >> ./temp_status.txt')
    elif step == 'step4':
        os.system(f'crab status -d ../m{mass}/crab_projects/crab_mUFO_ALP_m{mass}_step3 >> ./temp_status.txt')

def parseDB():
    with open('./temp_status.txt','r') as fl:
        lines = fl.readlines()
    
    for line in lines:
        if 'Output dataset' in line and 'URL' not in line:
            prevDB = line.strip().split()[-1]
            break
    
    os.remove('./temp_status.txt')

    return prevDB

def Unpack(mMasses):
    step = 'step1_NONE'

    for mass in mMasses:
        mMassPoint = convertMass(mass)

        # Produce the crab congiuration shell
        mtxt = loadStepTemplate(step)
        mtxt_proc = procMP(mMassPoint,mtxt)
        store(mMassPoint,step,mtxt_proc)

        # Run cmsDriver.py
        runCMSDriver(mMassPoint,step)

        execute(mMassPoint,step)

def stepThrough(mMasses,step):

    for mass in mMasses:
        mMassPoint = convertMass(mass)

        # Find previous database
        findDB(mMassPoint,step)
        prevDB = parseDB()

        # Produce the crab congiuration shell
        mtxt = loadStepTemplate(step)
        mtxt_proc = procMP(mMassPoint,mtxt,prevDB)
        store(mMassPoint,step,mtxt_proc)

        # Run cmsDriver.py
        runCMSDriver(mMassPoint,step)

        execute(mMassPoint,step)

def checkStatus(mMassPoints,step):
    for mass in mMassPoints:
        mMassPoint = convertMass(mass)

        os.system(f'crab status -d ../m{mMassPoint}/crab_projects/crab_mUFO_ALP_m{mMassPoint}_{step}/')

if __name__ == '__main__':

    #mMasses = [57.5,5,15,35,40,45,62]

    #mMasses = [55]
    #mMasses = [57.5] # <- Had to resubmit some jobs (Step2)
    mMasses = [62]
    stepThrough(mMasses,'step3')
    #checkStatus(mMasses,'step3')

    #mMasses = [15,35,45]
    #stepThrough(mMasses,'step4')
    #checkStatus(mMasses,'step4')

    #mMasses = [5,40,62] # <- Some jobs are missing for some reason (Step2)

    #Unpack(mMasses)

    #checkStatus(mMasses,'step2')
