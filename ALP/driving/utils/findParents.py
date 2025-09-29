#!/usr/bin/env python3

import os

with open('./mfiles.txt','r') as fl:
    files = fl.readlines()

output = []

for mfl in files:
    jobid = int(mfl.split('_')[-1].split('.')[0])
    mquery = f'\"parent file={mfl.rstrip()} instance=prod/phys03\"'

    #print(f'dasgoclient -query={mquery} > ./job_{jobid}_parents.txt')
    #os.system(f'dasgoclient -query={mquery}')
    os.system(f'dasgoclient -query={mquery} > ./temp.txt')

    with open('temp.txt','r') as fl:
        mflnm = fl.readlines()[0]
    
    output.append(f'{jobid}\t{mflnm}')

with open('./parents.txt','w') as fl:
    fl.writelines(output)
