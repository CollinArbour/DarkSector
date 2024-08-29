import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'mUFO_ALP_m52p5_step1'
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
config.Data.outputDatasetTag = 'mUFO_ALP_m52p5_step1'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/carbour/mc/alp/mUFO/m52p5/'
config.Data.publication = True

config.Data.inputDataset = '/CRAB_PrivateMC/carbour-mUFO_ALP_m52p5_step0-c288b964a52800503931221109d71d2c/USER'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
