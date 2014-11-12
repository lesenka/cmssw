#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

namespace gent {

  class GentTopCommonTestAnalyzer : public edm::EDAnalyzer {

      // Data members
      edm::EDGetTokenT< reco::GenParticleCollection > genParticlesToken_;

    public:

      // Constructors and destructor
      explicit GentTopCommonTestAnalyzer( const edm::ParameterSet& iConfig );
      ~GentTopCommonTestAnalyzer(){};

    private:

      // Functions
      virtual void beginJob() override;
      virtual void analyze( const edm::Event& iEvent, const edm::EventSetup& iSetup ) override;
      virtual void endJob() override;

  }; // class

} // namespace

using namespace gent;

GentTopCommonTestAnalyzer::GentTopCommonTestAnalyzer( const edm::ParameterSet& iConfig )
  : genParticlesToken_( consumes< reco::GenParticleCollection >( iConfig.getParameter< edm::InputTag >( "genParticles" ) ) )
{
}

void GentTopCommonTestAnalyzer::beginJob()
{
}

void GentTopCommonTestAnalyzer::analyze( const edm::Event& iEvent, const edm::EventSetup& iSetup )
{
  // Get input
  edm::Handle< reco::GenParticleCollection > genParticles;
  iEvent.getByToken( genParticlesToken_, genParticles );
}

void GentTopCommonTestAnalyzer::endJob()
{
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE( GentTopCommonTestAnalyzer );
