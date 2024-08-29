import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'mUFO_ALP_m55_step0'
config.General.transferLogs = True
#config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step1_NONE.py'
config.JobType.inputFiles = ['mUFO_ALP_m55_events.lhe']
#config.JobType.numCores=4

config.section_('Data')
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
config.Data.totalUnits = 10000
config.Data.publication = True
config.Data.outputDatasetTag = 'mUFO_ALP_m55_step0'
config.Data.outLFNDirBase = '/store/user/carbour/mc/alp/mUFO/m55'
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
