import FWCore.ParameterSet.Config as cms

gentTopCommonTestAnalyzer = cms.EDAnalyzer(
  "GentTopCommonTestAnalyzer"
  # Input
, genParticles = cms.InputTag( 'genParticles' )
)
