import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'mUFO_ALP_m45_step2'
config.General.transferLogs = True
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_DATAMIX_L1_DIGI2RAW_HLT.py'
config.JobType.maxMemoryMB = 10000
config.JobType.numCores=4

config.section_('Data')
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'mUFO_ALP_m45_step2'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/carbour/mc/alp/mUFO/m45/'
config.Data.publication = True
#config.Data.inputDataset = '/CRAB_PrivateMC/carbour-mALP_30_mUFO_step1-a4e0eb2292c6c18080b9bf7f1017caf8/USER'
config.Data.inputDataset = '/CRAB_PrivateMC/carbour-mUFO_ALP_m45_step1-a4e0eb2292c6c18080b9bf7f1017caf8/USER'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
