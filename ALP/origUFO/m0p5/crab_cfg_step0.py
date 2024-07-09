import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'mALP_0p5_origUFO_step0'
config.General.transferLogs = True
#config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step0.py'
config.JobType.inputFiles = ['origUFO_ALP_m0p5_events.lhe']
#config.JobType.numCores=4

config.section_('Data')
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
config.Data.totalUnits = 10000
config.Data.publication = True
config.Data.outputDatasetTag = 'mALP_0p5_origUFO_step0'
config.Data.outLFNDirBase = '/store/user/carbour/mc/alp/origUFO/m0p5'
#config.Data.userInputFiles = ['/store/user/carbour/alp/a0p5/alp_0p5_GEN-SIM.root']
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
