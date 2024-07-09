import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'mALP_30_origUFO_step2'
config.General.transferLogs = True
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2.py'
config.JobType.maxMemoryMB = 10000
config.JobType.numCores=4

config.section_('Data')
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'mALP_30_origUFO_step2'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/carbour/mc/alp/origUFO/m30/'
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/carbour-mALP_30_origUFO_step1-a4e0eb2292c6c18080b9bf7f1017caf8/USER'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
