import FWCore.ParameterSet.Config as cms
# from Configuration.ProcessModifiers.l1tracking_cff import *

layerListForPhase2 = ['BPix1+BPix2+BPix3+BPix4',
                       'BPix1+BPix2+BPix3+FPix1_pos','BPix1+BPix2+BPix3+FPix1_neg',
                       'BPix1+BPix2+FPix1_pos+FPix2_pos', 'BPix1+BPix2+FPix1_neg+FPix2_neg',
                       'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
                       'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
                       'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
                       'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
                       'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
                       'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg'
                       ]
layerListForPhase2Eta4 = layerListForPhase2 + ['FPix5_pos+FPix6_pos+FPix7_pos+FPix9_pos', 'FPix5_neg+FPix6_neg+FPix7_neg+FPix9_neg',
'FPix6_pos+FPix7_pos+FPix8_pos+FPix9_pos', 'FPix6_neg+FPix7_neg+FPix8_neg+FPix9_neg',
'FPix8_pos+FPix9_pos+FPix10_pos+FPix11_pos', 'FPix8_neg+FPix9_neg+FPix10_neg+FPix11_neg',
 'FPix11_pos+FPix9_pos+FPix10_pos+FPix12_pos', 'FPix9_neg+FPix10_neg+FPix11_neg+FPix12_neg']

tripletsLayers = ['BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix2_neg+FPix3_neg',
        'FPix2_pos+FPix3_pos+FPix4_pos',
        'FPix2_neg+FPix3_neg+FPix4_neg',
        'FPix3_pos+FPix4_pos+FPix5_pos',
        'FPix3_neg+FPix4_neg+FPix5_neg',
        'FPix4_pos+FPix5_pos+FPix6_pos',
        'FPix4_neg+FPix5_neg+FPix6_neg',
        'FPix5_pos+FPix6_pos+FPix7_pos',
        'FPix5_neg+FPix6_neg+FPix7_neg',
        'FPix6_pos+FPix7_pos+FPix8_pos',
        'FPix6_neg+FPix7_neg+FPix8_neg'
     ]


tripletsLayersEta4 = tripletsLayers +  ['BPix1+BPix2+FPix2_pos', 'BPix1+BPix2+FPix2_neg','BPix1+FPix1_pos+FPix3_pos',
                            'BPix1+FPix1_neg+FPix3_neg','FPix6_pos+FPix7_pos+FPix9_pos', 'FPix6_neg+FPix7_neg+FPix9_neg']


########################################################
############################ Customisers
##############
import RecoTracker.MkFit.mkFitInputConverter_cfi as mkFitInputConverter_cfi
import RecoTracker.MkFit.mkFitProducer_cfi as mkFitProducer_cfi
import RecoTracker.MkFit.mkFitOutputConverter_cfi as mkFitOutputConverter_cfi


def customizePixelTracksSoAonCPU(process) :

  from RecoLocalTracker.SiPixelRecHits.siPixelRecHitHostSoA_cfi import siPixelRecHitHostSoA as _siPixelRecHitFromSOA

  process.load("HeterogeneousCore.CUDAServices.CUDAService_cfi")
  process.load('RecoLocalTracker.SiPixelRecHits.siPixelRecHitHostSoA_cfi')
  process.load('RecoPixelVertexing.PixelTriplets.caHitNtupletCUDA_cfi')
  process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexCUDA_cfi')
  process.load('RecoPixelVertexing.PixelTrackFitting.pixelTrackProducerFromSoA_cfi')
  process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexFromSoA_cfi')

  process.siPixelRecHits = _siPixelRecHitFromSOA.clone()
  process.siPixelRecHits.src = 'siPixelClusters'
  process.siPixelRecHits.Upgrade = True
  process.siPixelRecHitsTask = cms.Task(process.siPixelRecHits)
  process.siPixelRecHits.convertToLegacy = True
  process.PixelCPEFastESProducer.Upgrade = True

  process.pixelTrackSoA = process.caHitNtupletCUDA.clone()
  process.pixelTrackSoA.onGPU = False
  process.pixelTrackSoA.pixelRecHitSrc = 'siPixelRecHits'#'siPixelRecHitHostSoA'
  process.pixelTrackSoA.isUpgrade = True

  process.hltPhase2PixelTracks = process.pixelTrackProducerFromSoA.clone()
  process.hltPhase2PixelTracksSeedLayers.BPix.HitProducer = 'siPixelRecHits'#"siPixelRecHitHostSoA"
  process.hltPhase2PixelTracksSeedLayers.FPix.HitProducer = 'siPixelRecHits'#"siPixelRecHitHostSoA"

  process.pixelVertexSoA = process.pixelVertexCUDA.clone()
  process.pixelVertexSoA.onGPU = False
  process.pixelVertexSoA.pixelTrackSrc = 'pixelTrackSoA'

  process.hltPhase2PixelVertices = process.pixelVertexFromSoA.clone()
  process.hltPhase2PixelTracks.pixelRecHitLegacySrc = 'siPixelRecHits'#'siPixelRecHitHostSoA'
  process.hltPhase2PixelVertices.TrackCollection = 'hltPhase2PixelTracks'




  process.hltPhase2PixelTracksSequence = cms.Sequence(
      process.pixelTrackSoA +
      process.hltPhase2PixelTracks
  )

  process.hltPhase2PixelVerticesSequence = cms.Sequence(
      process.pixelVertexSoA +
      process.hltPhase2PixelVertices +
      process.hltPhase2TrimmedPixelVertices
  )

  return process

def pixelQuadrupletsEta4(process):

    process.hltPhase2PixelTracksSeedLayers.layerList = cms.vstring(layerListForPhase2Eta4)

    return process

def pixelTriplets(process):

    process.hltPhase2PixelTracksSeedLayers.layerList = cms.vstring(tripletsLayers)
    process.hltPhase2PixelTracksHitDoublets.layerPairs = cms.vuint32( 0, 1)
    process.hltPhase2PixelTracksHitSeeds = cms.EDProducer( "CAHitTripletEDProducer",
        CAHardPtCut = cms.double( 0.5 ),
        SeedComparitorPSet = cms.PSet(
          clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "siPixelClusterShapeCache") # pixelVertices
        ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        doublets = cms.InputTag( "hltPhase2PixelTracksHitDoublets" ),
        # fitFastCircle = cms.bool( True ),
        CAThetaCut = cms.double( 0.003 ), # 0.002 ),
        maxChi2 = cms.PSet(
            enabled = cms.bool(True),
            pt1 = cms.double(0.8),
            pt2 = cms.double(8),
            value1 = cms.double(100),
            value2 = cms.double(6)
        ),
        CAPhiCut = cms.double( 0.06 ),
        useBendingCorrection = cms.bool( True ),
        # fitFastCircleChi2Cut = cms.bool( True )#,
    )
    return process

def customizeL1TracksStepToMkFit(procaess):

    process.hltPhase2L1TracksCandidatesMkFitInput = mkFitInputConverter_cfi.mkFitInputConverter.clone(
            seeds = "hltPhase2L1TrackSeedsFromL1Tracks",
        )

    process.hltPhase2L1TracksCandidatesMkFit = mkFitProducer_cfi.mkFitProducer.clone(
            hitsSeeds = "hltPhase2L1TracksCandidatesMkFitInput",
        )

    process.hltPhase2L1TracksCandidates = mkFitOutputConverter_cfi.mkFitOutputConverter.clone(
        seeds = "hltPhase2L1TrackSeedsFromL1Tracks",
        hitsSeeds = "hltPhase2L1TracksCandidatesMkFitInput",
        tracks = "initialStepTrackCandidatesMkFit",
    )


    # proccess.siPixelClusters =
    process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1TracksCandidatesMkFitInput,
                              process.hltPhase2L1TracksCandidatesMkFit)

    return process

def customizeGeneralTracksToInitialL1TracksStep(process,timing):

    #process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1TrackStepClusters)

    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.initial_l1tracks])

    if not timing:
        process.schedule.extend([process.vertexing, process.prevalidation_l1initial,
                                          process.validation_l1initial, process.dqm_l1initial])

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('initialStep','ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2InitialStepTracksSelectionHighPurity","hltPhase2L1TracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
    "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp")

    return process

def customizeGeneralTracksToInitialL1TracksStepMasking(process):

    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.initial_l1tracks])

    if not timing:
        process.schedule.extend([process.vertexing, process.prevalidation_l1initial,
        process.validation_l1initial, process.dqm_l1initial])

    process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1StepSeedClusterMask)
    process.hltPhase2L1TracksCutClassifier.vertices = cms.InputTag("hltPhase2L1TracksStepPrimaryVertices")

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('initialStep','ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2InitialStepTracksSelectionHighPurity","hltPhase2L1TracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
    "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp")

    process.hltPhase2PixelTracksSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")
    process.hltPhase2PixelTracksSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")

    return process

def customizeGeneralTracksToInitialL1TracksStepMasking(process):

    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.initial_l1tracks])

    if not timing:
            process.schedule.extend([process.vertexing, process.prevalidation_l1initial,
                                          process.validation_l1initial, process.dqm_l1initial])

    process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1TrackStepClusters)
    process.hltPhase2L1TrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2L1TrackStepClusters")
    process.hltPhase2L1TrackStepClusters.trajectories = cms.InputTag("hltPhase2InitialStepTracks")
    process.hltPhase2L1TracksCutClassifier.vertices = cms.InputTag("hltPhase2L1TracksStepPrimaryVertices")

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('initialStep','ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2InitialStepTracksSelectionHighPurity","hltPhase2L1TracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
    "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp")

    process.hltPhase2PixelTracksSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")
    process.hltPhase2PixelTracksSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")

    return process

##PixelTracks + Masking + L1 Tracks + Masking + Recovery Seeded by L1
def pixel_l1_recovery(process,timing):


    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pixeltriplet_l1])

    if not timing:
        process.schedule.extend([process.prevalidation_l1initial,
                                          process.validation_l1initial, process.dqm_l1initial])

    ##masking with pixel tracks
    process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1TrackStepClusters)
    process.hltPhase2L1TrackStepClusters.trajectories = cms.InputTag("hltPhase2PixelTracks")
    process.hltPhase2L1TrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2L1TrackStepClusters")

    ##pixel vertices for classification
    process.hltPhase2L1TracksCutClassifier.vertices = cms.InputTag("hltPhase2L1TracksStepPrimaryVertices")

    ##masking with l1 tracks
    process.hltPhase2InitialStepClusters.trajectories = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2InitialStepClusters")

    ##general tracks - recovery + l1
    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('hltIter0','initialStep')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1CtfTracks","hltPhase2InitialStepTracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,0.9)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("loose"),
                                                                     cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
    "hltPhase2GeneralTracks","hltPhase2CutsRecoTracksL1",
    "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp",
    "hltPhase2CutsRecoTracksL1StepByOriginalAlgo","hltPhase2CutsRecoTracksL1StepByOriginalAlgoHp")

    # process.hltPhase2PixelTracksSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")
    # process.hltPhase2PixelTracksSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")

    return process

def l1_pixel_recovery(process,timing):


    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.l1_pixel_reco])

    if not timing:
        process.schedule.extend([process.prevalidation_l1initial,
                                      process.validation_l1initial, process.dqm_l1initial])

    process.hltPhase2PixelTrackClusters.trajectories = cms.InputTag("hltPhase2L1CtfTracks")

    process.hltPhase2PixelTracksSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2PixelTrackClusters")
    process.hltPhase2PixelTracksSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2PixelTrackClusters")

    ##masking with pixel tracks
    # process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1TrackStepClusters)
    # process.hltPhase2L1TrackStepClusters.trajectories = cms.InputTag("hltPhase2PixelTracks")
    # process.hltPhase2L1TrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2L1TrackStepClusters")

    ##pixel vertices for classification
    process.hltPhase2L1TracksCutClassifier.vertices = cms.InputTag("hltPhase2PixelVertices")

    ##masking with l1 tracks
    # process.hltPhase2InitialStepClusters.trajectories = cms.InputTag("hltPhase2L1CtfTracks")
    # process.hltPhase2InitialStepTrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2InitialStepClusters")

    ##general tracks - recovery + l1
    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('hltIter0','initialStep')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1CtfTracks","hltPhase2InitialStepTracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag(""),
                                                                     cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
    "hltPhase2GeneralTracks","hltPhase2CutsRecoTracksL1",
    "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp",
    "hltPhase2CutsRecoTracksL1StepByOriginalAlgo","hltPhase2CutsRecoTracksL1StepByOriginalAlgoHp")

    return process

def l1_pixel_recovery_triplets(process,timing):


    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.l1_pixel_reco_triplets])

    process.hltPhase2PixelTrackClusters.trajectories = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2PixelTracksSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2PixelTrackClusters")
    process.hltPhase2PixelTracksSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2PixelTrackClusters")


    #process.hltPhase2HighPtTripletStepSeedLayers.layerList = cms.vstring(layerListForPhase2)
    #process.hltPhase2HighPtTripletStepHitDoublets.layerPairs = cms.vuint32(0, 1, 2)
    # process.hltPhase2HighPtTripletStepHitTriplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    #     CAHardPtCut = cms.double( 0.8 ),
    #     SeedComparitorPSet = cms.PSet(
    #       clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
    #       ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
    #       clusterShapeCacheSrc = cms.InputTag( "siPixelClusterShapeCache") # pixelVertices
    #     ),
    #     extraHitRPhitolerance = cms.double( 0.032 ),
    #     doublets = cms.InputTag( "hltPhase2HighPtTripletStepHitDoublets" ),
    #     fitFastCircle = cms.bool( True ),
    #     CAThetaCut = cms.double( 0.0012 ), # 0.002 ),
    #     maxChi2 = cms.PSet(
    #       value2 = cms.double( 50.0 ),
    #       value1 = cms.double( 200.0 ),
    #       pt1 = cms.double( 0.7 ),
    #       enabled = cms.bool( True ),
    #       pt2 = cms.double( 2.0 )
    #     ),
    #     CAPhiCut = cms.double( 0.2 ),
    #     useBendingCorrection = cms.bool( True ),
    #     fitFastCircleChi2Cut = cms.bool( True )#,
    # )

    # process.hltPhase2HighPtTripletStepTrackingRegions = cms.EDProducer( "GlobalTrackingRegionFromBeamSpotEDProducer",
    #     RegionPSet = cms.PSet(
    #       nSigmaZ = cms.double( 5.0 ),
    #       beamSpot = cms.InputTag( "offlineBeamSpot"),
    #       ptMin = cms.double( 0.9 ), # previous 0.8
    #       originRadius = cms.double( 0.1 ),
    #       precise = cms.bool( True )
    #     )
    # )
    process.hltPhase2HighPtTripletStepClusters.TrackQuality  = cms.string('')
    process.hltPhase2HighPtTripletStepClusters.trajectories = cms.InputTag("hltPhase2InitialStepTracks")
    process.hltPhase2HighPtTripletStepClusters.oldClusterRemovalInfo = cms.InputTag("hltPhase2PixelTrackClusters")
    process.hltPhase2HighPtTripletStepSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2HighPtTripletStepClusters")
    process.hltPhase2HighPtTripletStepSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2HighPtTripletStepClusters")

    ##masking with pixel tracks
    # process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1TrackStepClusters)
    # process.hltPhase2L1TrackStepClusters.trajectories = cms.InputTag("hltPhase2PixelTracks")
    # process.hltPhase2L1TrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2L1TrackStepClusters")

    ##pixel vertices for classification
    process.hltPhase2L1TracksCutClassifier.vertices = cms.InputTag("hltPhase2PixelVertices")

    ##masking with l1 tracks
    # process.hltPhase2InitialStepClusters.trajectories = cms.InputTag("hltPhase2L1CtfTracks")
    # process.hltPhase2InitialStepTrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2InitialStepClusters")

    ##general tracks - recovery + l1
    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('hltIter0','initialStep','highPtTripletStep')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1CtfTracks","hltPhase2InitialStepTracksSelectionHighPurity","hltPhase2HighPtTripletStepTracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag(""),
                                                                     cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2HighPtTripletStepTracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1,2)

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    return process

def customizeTripletL1(process,timing=False):


    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.triplet_l1tracks,
                                            process.prevalidation_l1trip,
                                            process.validation_l1initial, process.dqm_l1trip])


    process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1StepSeedClusterMask)
    # process.hltPhase2L1TracksCutClassifier.vertices = cms.InputTag("hltPhase2L1TracksStepPrimaryVertices")
    process.hltPhase2HighPtTripletStepClusters.trajectories = cms.InputTag("hltPhase2L1TracksSelectionHighPurity")
    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('highPtTripletStep','ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2HighPtTripletStepTracksSelectionHighPurity","hltPhase2L1TracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2HighPtTripletStepTracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    # process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    # process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag("hltPhase2GeneralTracks","hltPhase2CutsRecoTracksL1Step",
    "hltPhase2CutsRecoTracksHighPtTripletStep" ,
    "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask","hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",
    "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp","hltPhase2CutsRecoTracksL1StepByOriginalAlgo")

    # process.hltPhase2HighPtTripletStepSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")
    # process.hltPhase2HighPtTripletStepSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")

    return process

def customizeOriginal_v7(process,timing):

    # process.siPixelClusters.vertices = "hltPhase2PixelVertices"
    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.original_v7])

    if not timing:
        process.schedule.extend([process.vertexing, process.prevalidation_original,
            process.validation_original, process.dqm_original])


def customizeOriginal_v6(process,timing):

        process.schedule = cms.Schedule(*[process.raw2digi_step,process.original_v6])

        if not timing:
            process.schedule.extend([process.vertexing, process.prevalidation_original,
                process.validation_original, process.dqm_original])

def customizeGeneralTracksToPixelL1TracksStep(process,timing):

    if not timing:
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
                                      process.vertexing, process.prevalidation_purel1,
                                      process.validation_l1initial, process.dqm_purel1])

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('ctf','hltPixel')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1CtfTracks","hltPhase2PixelTracks")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2L1TracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2PixelTracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag("hltPhase2GeneralTracks",
    "hltPhase2CutsRecoTracksHighPtTripletStep" ,
    "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",
    "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp")

    return process

def customizeGeneralTracksToPixelTripletL1TracksStep(process,timing):

    process.hltPhase2PixelTracksHitSeeds = cms.EDProducer( "CAHitTripletEDProducer",
        CAHardPtCut = cms.double( 0.5 ),
        SeedComparitorPSet = cms.PSet(
          clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "siPixelClusterShapeCache") # pixelVertices
        ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        doublets = cms.InputTag( "hltPhase2PixelTracksHitDoublets" ),
        # fitFastCircle = cms.bool( True ),
        CAThetaCut = cms.double( 0.0012 ), # 0.002 ),
        maxChi2 = cms.PSet(
          value2 = cms.double( 50.0 ),
          value1 = cms.double( 200.0 ),
          pt1 = cms.double( 0.7 ),
          enabled = cms.bool( True ),
          pt2 = cms.double( 2.0 )
        ),
        CAPhiCut = cms.double( 0.18 ),
        useBendingCorrection = cms.bool( True ),
        # fitFastCircleChi2Cut = cms.bool( True )#,
    )

    process.hltPhase2PixelTracksHitDoublets.layerPairs = cms.vuint32( 0, 1 )
    process.hltPhase2PixelTracksSeedLayers.layerList = cms.vstring(tripletsLayers)

    if timing:
        # process.initial_l1tracks = 0
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
                                          process.vertexing])
    else:
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
                                          process.vertexing, process.prevalidation_purel1,
                                          process.validation_l1initial, process.dqm_purel1])


    #l1tracking.toReplaceWith(process.hltPhase2PixelTracksHitQuadruplets,process.hltPhase2PixelTracksHitTriplets)

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('ctf','hltPixel')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1CtfTracks","hltPhase2PixelTracks")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2L1TracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2PixelTracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag("hltPhase2GeneralTracks")

    return process

def customizeGeneralTracksToPureL1TracksStep(process,timing):

    process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
                                          process.vertexing])
    if not timing:
                process.schedule.extend([process.prevalidation_purel1,
                                          process.validation_purel1, process.dqm_purel1])



    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1TracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag("hltPhase2GeneralTracks")

    return process

def customize_pre7(process):

    gooppvtx_60 = cms.PSet(GoodPVtxBin = cms.int32(60),GoodPVtxMax = cms.double(60.0),GoodPVtxMin = cms.double(0.0))
    gooppvtx_200 = cms.PSet(GoodPVtxBin = cms.int32(200),GoodPVtxMax = cms.double(200.0),GoodPVtxMin = cms.double(0.0))
    npvtx = cms.PSet(NTrkPVtxBin = cms.int32(200), NTrkPVtxMin = cms.double( 0.), NTrkPVtxMax = cms.double(200.))
    sumptvtx = cms.PSet(SumPtPVtxBin = cms.int32(200), SumPtPVtxMin = cms.double( 0.), SumPtPVtxMax = cms.double(1000.))

    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPtRange0to1.GoodPVtx = gooppvtx_60
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPt1.GoodPVtx = gooppvtx_200
    process.hltPhase2TrackSeedMonhighPtTripletStep.GoodPVtx = gooppvtx_200
    process.hltPhase2TrackSeedMoninitialStep.GoodPVtx = gooppvtx_200
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPV0p1.GoodPVtx = gooppvtx_60
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.GoodPVtx = gooppvtx_60

    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPtRange0to1.SumPtPVtx = sumptvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPt1.v = sumptvtx
    process.hltPhase2TrackSeedMonhighPtTripletStep.SumPtPVtx = sumptvtx
    process.hltPhase2TrackSeedMoninitialStep.SumPtPVtx = sumptvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPV0p1.SumPtPVtx = sumptvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.SumPtPVtx = sumptvtx

    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPtRange0to1.NTrkPVtx = npvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPt1.NTrkPVtx = npvtx
    process.hltPhase2TrackSeedMonhighPtTripletStep.NTrkPVtx = npvtx
    process.hltPhase2TrackSeedMoninitialStep.NTrkPVtx = npvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPV0p1.NTrkPVtx = npvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.NTrkPVtx = npvtx



    return process

def customize_11_1_0(process):

    customize_pre7(process)

    ntrk2d = cms.PSet(NTrk2DBin = cms.int32(50), NTrk2DMax = cms.double(1999.5), NTrk2DMin = cms.double(-0.5))

    process.hltPhase2TrackSeedMonhighPtTripletStep.NTrk2D = ntrk2d
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.NTrk2D = ntrk2d
    process.hltPhase2TrackSeedMoninitialStep.NTrk2D = ntrk2d
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPV0p1.NTrk2D = ntrk2d
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPt1.NTrk2D = ntrk2d

    process.hltPhase2TrackSeedMonhighPtTripletStep.forceSCAL = cms.bool(True)
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.forceSCAL = cms.bool(True)
    process.hltPhase2TrackSeedMoninitialStep.forceSCAL = cms.bool(True)
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPV0p1.forceSCAL = cms.bool(True)
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPt1.forceSCAL = cms.bool(True)


    return process
