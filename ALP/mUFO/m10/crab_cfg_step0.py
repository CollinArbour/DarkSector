import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'mALP_10_mUFO_step0'
config.General.transferLogs = True
#config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step0.py'
config.JobType.inputFiles = ['mUFO_ALP_m10_events.lhe']
#config.JobType.numCores=4

config.section_('Data')
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
config.Data.totalUnits = 10000
config.Data.publication = True
config.Data.outputDatasetTag = 'mALP_10_mUFO_step0'
config.Data.outLFNDirBase = '/store/user/carbour/mc/alp/mUFO/m10'
#config.Data.userInputFiles = ['/store/user/carbour/alp/a10/alp_10_GEN-SIM.root']
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
