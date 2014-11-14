import FWCore.ParameterSet.Config as cms

# Process
process = cms.Process( "TEST" )

# Logging
process.load( "FWCore.MessageLogger.MessageLogger_cfi" )
process.options = cms.untracked.PSet(
  wantSummary = cms.untracked.bool( True )
)

# Input
from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
process.source = cms.Source(
  "PoolSource"
, fileNames = filesRelValProdTTbarAODSIM
)
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32( 100 )
)

# Conditions
process.load( "Configuration.Geometry.GeometryIdeal_cff" )
process.load( "Configuration.StandardSequences.FrontierConditions_GlobalTag_cff" )
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag( process.GlobalTag, 'auto:run2_mc' )
process.load( "Configuration.StandardSequences.MagneticField_cff" )

# Analyzer
process.load( "GentTopAnalysis.XSection.gentTopXSectionTestAnalyzer_cfi" )
process.testPath = cms.Path(
  process.gentTopXSectionTestAnalyzer
)

# Output
process.out = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string('gentTopXSectionTest.root'),
  outputCommands = cms.untracked.vstring(
    'drop *'
  , 'keep *_genParticles_*_*'
  )
)

process.outpath = cms.EndPath(
  process.out
)
