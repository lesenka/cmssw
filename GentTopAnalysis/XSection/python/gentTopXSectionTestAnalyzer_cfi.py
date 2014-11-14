import FWCore.ParameterSet.Config as cms

gentTopXSectionTestAnalyzer = cms.EDAnalyzer(
  "GentTopXSectionTestAnalyzer"
  # Input
, genParticles = cms.InputTag( 'genParticles' )
)
