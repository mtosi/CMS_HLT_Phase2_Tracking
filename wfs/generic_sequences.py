import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Reconstruction_cff import *
from RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi import *
from RecoTracker.MeasurementDet.MeasurementTrackerESProducer_cfi import *


############# ordered setup

ecalUncalibRecHitSequence = cms.Sequence(
    bunchSpacingProducer +
    ecalMultiFitUncalibRecHit +
    ecalDetIdToBeRecovered
)

caloLocalReco = cms.Sequence(
    ecalUncalibRecHitSequence +
    ecalRecHit +
    hbhereco +
    hfprereco +
    hfreco + #uses hfprereco
    horeco
)

itLocalReco = cms.Sequence(
    siPhase2Clusters +
    siPixelClusters +
    siPixelClusterShapeCache +
    siPixelRecHits
)

TrackerRecoGeometryESProducer.trackerGeometryLabel = cms.untracked.string("")

trackerGeoTask = cms.Task(TrackerRecoGeometryESProducer)
trackerMeaTask = cms.Task(MeasurementTracker)

trackerGeo = cms.Sequence(trackerGeoTask)
trackerMea = cms.Sequence(trackerMeaTask)

otLocalReco = cms.Sequence(
    trackerGeo+
    trackerMea+
    MeasurementTrackerEvent
)

from SimFastTiming.FastTimingCommon.mtdDigitizer_cfi import mtdDigitizer
hltMTDUncalibratedRecHits = cms.EDProducer("MTDUncalibratedRecHitProducer",
    barrel = cms.PSet(
       algoName = cms.string("BTLUncalibRecHitAlgo"),
       adcNbits = mtdDigitizer.barrelDigitizer.ElectronicsSimulation.adcNbits,
       adcSaturation = mtdDigitizer.barrelDigitizer.ElectronicsSimulation.adcSaturation_MIP,
       toaLSB_ns = mtdDigitizer.barrelDigitizer.ElectronicsSimulation.toaLSB_ns,
       timeResolutionInNs = cms.string("0.308*pow(x,-0.4175)"), # [ns]
       timeCorr_p0 = cms.double( 2.21103),
       timeCorr_p1 = cms.double(-0.933552),
       timeCorr_p2 = cms.double( 0.),
       c_LYSO = cms.double(13.846235)     # in unit cm/ns
    ),
    endcap = cms.PSet(
       algoName      = cms.string("ETLUncalibRecHitAlgo"),
       adcNbits      = mtdDigitizer.endcapDigitizer.ElectronicsSimulation.adcNbits,
       adcSaturation = mtdDigitizer.endcapDigitizer.ElectronicsSimulation.adcSaturation_MIP,
       toaLSB_ns     = mtdDigitizer.endcapDigitizer.ElectronicsSimulation.toaLSB_ns,
       tofDelay      = mtdDigitizer.endcapDigitizer.DeviceSimulation.tofDelay,
       timeResolutionInNs = cms.string("0.039") # [ns]
    ),
    barrelDigis = cms.InputTag('mix:FTLBarrel'),
    endcapDigis = cms.InputTag('mix:FTLEndcap'),
    BarrelHitsName = cms.string('FTLBarrel'),
    EndcapHitsName = cms.string('FTLEndcap')
)

#from Configuration.Eras.Modifier_phase2_etlV4_cff import phase2_etlV4
#phase2_etlV4.toModify(_endcapAlgo, thresholdToKeep = 0.005, calibrationConstant = 0.015 )
hltMTDRecHits = cms.EDProducer("MTDRecHitProducer",
    barrel = cms.PSet(
       algoName = cms.string("MTDRecHitAlgo"),
       thresholdToKeep = cms.double(1.),          # MeV
       calibrationConstant = cms.double(0.03125), # MeV/pC
    ),
    endcap = cms.PSet(
       algoName = cms.string("MTDRecHitAlgo"),
       thresholdToKeep = cms.double(0.0425),    # MeV
       calibrationConstant = cms.double(0.085), # MeV/MIP
    ),
    barrelUncalibratedRecHits = cms.InputTag('hltMTDUncalibratedRecHits:FTLBarrel'),
    endcapUncalibratedRecHits = cms.InputTag('hltMTDUncalibratedRecHits:FTLEndcap'),
    BarrelHitsName = cms.string('FTLBarrel'),
    EndcapHitsName = cms.string('FTLEndcap'),
)

hltMTDClusters = cms.EDProducer('MTDClusterProducer',
  srcBarrel = cms.InputTag('hltMTDRecHits', 'FTLBarrel'),
  srcEndcap = cms.InputTag('hltMTDRecHits', 'FTLEndcap'),
  BarrelClusterName = cms.string('FTLBarrel'),
  EndcapClusterName = cms.string('FTLEndcap'),
  ClusterMode = cms.string('MTDThresholdClusterizer'),
  HitThreshold = cms.double(0),
  SeedThreshold = cms.double(0),
  ClusterThreshold = cms.double(0),
  TimeThreshold = cms.double(10),
  PositionThreshold = cms.double(-1),
  mightGet = cms.optional.untracked.vstring
)

hltMTDTrackingRecHits = cms.EDProducer('MTDTrackingRecHitProducer',
  barrelClusters = cms.InputTag('hltMTDClusters', 'FTLBarrel'),
  endcapClusters = cms.InputTag('hltMTDClusters', 'FTLEndcap'),
  mightGet = cms.optional.untracked.vstring
)


## mtd local reco
mtdLocalReco = cms.Sequence(
    hltMTDUncalibratedRecHits +
    hltMTDRecHits + 
    hltMTDClusters +
    hltMTDTrackingRecHits
)
