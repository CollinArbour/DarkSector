#!/usr/bin/env python3

import os
import argparse

_allowedSteps = ['step0','step1_NONE','step1','step2','step3','step4']
_steps=['step1_NONE.py',\
        'Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff_py_GEN_SIM.py',\
        'step2_DIGI_DATAMIX_L1_DIGI2RAW_HLT.py',\
        'step3_RAW2DIGI_L1Reco_RECO_RECOSIM.py',\
        'step4_PAT.py']

_PU = ''

def verifyOptions(args):
    if args.step not in _allowedSteps:
        raise ValueError(f'{args.step} is not a valid step')
    if args.noPileUp:
        global _PU
        print('Not using premixed PileUp')
        _PU = '_noPU'

def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m','--massPoints',nargs='+',dest='massPoints',help='Which mass points to submit for (numerical)')
    parser.add_argument('-s','--step',dest='step',help='Which step to submit for')
    parser.add_argument('-it','--inTag',dest='inTag',default=None,help='Tag for in put dataset')
    parser.add_argument('-ot','--outTag',dest='outTag',default=None,help='Tag to use for out put dataset')
    parser.add_argument('-noPU','--noPileUp',dest='noPileUp',default=False,action='store_true',help='Include if you do not want to use PU in step2')
    
    args = parser.parse_args()
    verifyOptions(args)

    return args

def convertMass(mass):
    msplit = str(mass).split('.')
    if len(msplit) == 1:
        return msplit[0]
    else:
        return f'{msplit[0]}p{msplit[1]}'

def mkID(mMassPoint,mTag=None):
    mID = f'm{mMassPoint}'
    if mTag:
        mID += f'_{mTag}'
    return mID
    
def loadStepTemplate(step):
    if step != 'step2':
        flnm = f'./templates/crab_cfg_{step}.txt'
    else:
        flnm = f'./templates/crab_cfg_{step}{_PU}.txt'
        print(f'Loading Crab template: {flnm}')

    with open(flnm,'r') as fl:
        mtxt = fl.readlines()
    return mtxt

def procMP(mMassPoint,txt_data,mPrevDB='',mTag=None):

    mID = mkID(mMassPoint,mTag=mTag)

    mtxt_proc = []

    if mPrevDB:
        mPrevDB = f'\'{mPrevDB}\''
    for line in txt_data:
        if '{mMassPoint}' in line:
            mtxt_proc.append(line.format(mMassPoint=mMassPoint))
        elif '{mID}' in line:
            mtxt_proc.append(line.format(mID=mID))
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
        os.system(f'./driverCmds/step0_unpack.sh ../m{mass}/ {mass}')
    elif step == 'step1':
        os.system(f'./driverCmds/step1_lhe_to_root.sh ../m{mass}/ {mass}')
    elif step == 'step2':
        os.system(f'./driverCmds/step2_digi_hlt{_PU}.sh ../m{mass}/ {mass}')
    elif step == 'step3':
        os.system(f'./driverCmds/step3_reco.sh ../m{mass}/ {mass}')
    elif step == 'step4':
        os.system(f'./driverCmds/step4_miniAOD.sh ../m{mass}/ {mass}')

def findDB(mMassPoint,step,mTag=None):

    mID = mkID(mMassPoint,mTag=mTag)

    if step == 'step1':
        os.system(f'crab status -d ../m{mMassPoint}/crab_mUFO_ALP_{mID}_step0 >> ./temp_status.txt')
    elif step == 'step2':
        os.system(f'crab status -d ../m{mMassPoint}/crab_projects/crab_mUFO_ALP_{mID}_step1 >> ./temp_status.txt')
    elif step == 'step3':
        os.system(f'crab status -d ../m{mMassPoint}/crab_projects/crab_mUFO_ALP_{mID}_step2 >> ./temp_status.txt')
    elif step == 'step4':
        os.system(f'crab status -d ../m{mMassPoint}/crab_projects/crab_mUFO_ALP_{mID}_step3 >> ./temp_status.txt')

def parseDB():
    with open('./temp_status.txt','r') as fl:
        lines = fl.readlines()
    
    for line in lines:
        if 'Output dataset' in line and 'URL' not in line:
            prevDB = line.strip().split()[-1]
            break
    
    os.remove('./temp_status.txt')

    return prevDB

def Unpack(mMasses,mTag=None):
    step = 'step1_NONE'
    for mass in mMasses:

        mMassPoint = convertMass(mass)

        # Produce the crab congiuration shell
        mtxt = loadStepTemplate(step)
        mtxt_proc = procMP(mMassPoint,mtxt,mTag=mTag)
        store(mMassPoint,step,mtxt_proc)

        # Run cmsDriver.py
        runCMSDriver(mMassPoint,step)

        execute(mMassPoint,step)

def stepThrough(mMasses,step,inTag=None,outTag=None):

    # If LHE file still needs to be unpacked, do that first
    if step == 'step0' or step == 'step1_NONE':
        Unpack(mMasses,mTag=outTag)
        return

    for mass in mMasses:
        mMassPoint = convertMass(mass)

        # Find previous database
        findDB(mMassPoint,step,mTag=inTag)
        prevDB = parseDB()

        # Produce the crab congiuration shell
        mtxt = loadStepTemplate(step)
        mtxt_proc = procMP(mMassPoint,mtxt,prevDB,mTag=outTag)
        store(mMassPoint,step,mtxt_proc)

        # Run cmsDriver.py
        runCMSDriver(mMassPoint,step)

        execute(mMassPoint,step)
    return

def checkStatus(mMassPoints,step):
    for mass in mMassPoints:
        mMassPoint = convertMass(mass)

        os.system(f'crab status -d ../m{mMassPoint}/crab_projects/crab_mUFO_ALP_m{mMassPoint}_{step}/')

def main():
    args = arg_parse()

    if not args.outTag:
        args.outTag = args.inTag

    #Unpack(mMasses)
    stepThrough(args.massPoints,args.step,inTag=args.inTag,outTag=args.outTag)


if __name__ == '__main__':
    main()
