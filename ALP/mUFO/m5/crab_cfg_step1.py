import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'mUFO_ALP_m5_step1'
config.General.transferLogs = True
config.General.workArea = 'crab_projects'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff_py_GEN_SIM.py'
config.JobType.maxMemoryMB = 10000
config.JobType.numCores=4

config.section_('Data')
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'mUFO_ALP_m5_step1'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/carbour/mc/alp/mUFO/m5/'
config.Data.publication = True

#config.Data.inputDataset = '/CRAB_PrivateMC/carbour-mALP_0p5_mUFO_step0-3f22eb42fbc8c953391827da6f10333b/USER'
config.Data.inputDataset = '/CRAB_PrivateMC/carbour-mUFO_ALP_m5_step0-3f22eb42fbc8c953391827da6f10333b/USER'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
