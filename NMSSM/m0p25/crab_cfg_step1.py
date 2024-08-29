import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'NMSSM_m0p25_step1'
config.General.transferLogs = True
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'S1_RunIII_NMSSM_mA_0p25_step1_cfg.py'
config.JobType.maxMemoryMB = 10000
config.JobType.numCores=8

config.section_('Data')
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'NMSSM_m0p25_step1'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/carbour/mc/NMSSM/m0p25/'
config.Data.publication = True

config.Data.inputDataset = '/CRAB_PrivateMC/carbour-NMSSM_m0p25_step0-7362a64ddcd66c2ac4fdf1cb438a5f6a/USER'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'