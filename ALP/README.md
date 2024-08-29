# Warning
Only mUFO ALP samples: m52p5, m55, m57p5 have been created on `CMSSW_14_0_5` version

# Instructions for producing ALP Monte Carlo
For running Monte Carlo Production on ALP samples follow these steps:

Copy LHE file to your desired folder.

## Unpack LHE
```
cmsDriver.py step1 --filein file:mUFO_ALP_m52p5_events.lhe --fileout file:mUFO_ALP_m52p5_events.root --mc --eventcontent LHE --datatier LHE --conditions 124X_mcRun3_2022_realistic_postEE_v1 --step NONE --era Run3 -n 10000 --no_exec
```

# Using CRAB to submit said jobs

## Unpack LHE
Inorder to split the jobs by number of events its is best to start here

```
cmsenv
voms-proxy-init -voms cms -rfc --valid 168:0
```


# To Do
+ [ ] Improve the template generation code
