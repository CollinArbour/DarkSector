import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'origALP_0p5_mUFO_step4'
config.General.transferLogs = True
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4.py'
config.JobType.maxMemoryMB = 10000
config.JobType.numCores=4

config.section_('Data')
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'origALP_0p5_mUFO_step4'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/carbour/mc/alp/mUFO/m0p5/'
config.Data.publication = True

config.Data.inputDataset = '/CRAB_PrivateMC/carbour-mALP_0p5_origUFO_step3-59a22edf0600a784f6c900595d24e883/USER'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
