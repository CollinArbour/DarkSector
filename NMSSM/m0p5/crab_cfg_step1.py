import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'NMSSM_m0p5_step1'
config.General.transferLogs = True
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step1.py'
config.JobType.maxMemoryMB = 10000
config.JobType.numCores=8

config.section_('Data')
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'NMSSM_m0p5_step1'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/carbour/mc/NMSSM/m0p5/'
config.Data.publication = True

config.Data.inputDataset = '/CRAB_PrivateMC/carbour-NMSSM_m0p5_step0-ee18b858813a9051a89a1b5997e11fd7/USER'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
