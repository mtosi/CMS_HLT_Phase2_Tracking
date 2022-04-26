import FWCore.ParameterSet.Config as cms
from  Configuration.StandardSequences.Validation_cff import *
from validation_modules import *
from prevalidation_modules import *

hltTracksValidationTruth = cms.Sequence(hltTPClusterProducer+hltTrackAssociatorByHits+trackingParticleNumberOfLayersProducer)

hltMultiTrackValidation = cms.Sequence(
    hltTracksValidationTruth
    + hltPhase2TrackValidator
)

validation_original = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly
                              +hltPhase2TrackValidatorTrackingOnly
                              #hltPhase2TrackValidatorTPPtLess09Standalone
                              +hltPhase2TrackValidatorFromPVStandalone
                             #  +hltPhase2TrackValidatorFromPVAllTPStandalone
                              #+hltPhase2TrackValidatorAllTPEfficStandalone)
                               +hltPhase2TrackValidatorBHadronTrackingOnly)
                             # +hltPhase2TrackValidatorSeedingTrackingOnly)

validation_mtd = cms.Path(
    hltPhase2TrackValidatorPixelTrackingOnly
    +hltPhase2TrackValidatorTrackingOnly
    +hltPhase2TrackValidatorFromPVStandalone
    +hltPhase2TrackValidatorBHadronTrackingOnly
    +hltPhase2TrackValidatorPixelTrackExtendedWithMTD
)

validation_purel1 = cms.Path(hltPhase2TrackValidatorL1)

validation_l1initial = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidatorTrackingOnly + hltPhase2TrackValidatorL1)

validation_l1trip = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidatorTrackingOnly + hltPhase2TrackValidatorL1 +hltPhase2TrackValidatorFromPVStandalone +hltPhase2TrackValidatorBHadronTrackingOnly)

validation_base = cms.EndPath(hltMultiTrackValidation + hltTrackAssociatorByHits)

validation_pixel = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly)

validation_all = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidatorTrackingOnly + hltPhase2TrackValidatorL1)
