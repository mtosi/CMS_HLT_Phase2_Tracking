import FWCore.ParameterSet.Config as cms
from  Configuration.StandardSequences.Validation_cff import quickTrackAssociatorByHits, quickTrackAssociatorByHits, tpClusterProducer
from  Configuration.StandardSequences.Validation_cff import trackingParticlesBHadron, simHitTPAssocProducer, trackingParticlesConversion
from  Configuration.StandardSequences.Validation_cff import trackingParticleNumberOfLayersProducer

####################################################
########################## Pixel Tracks
#############

hltPhase2PixelVertexAssociatorByPositionAndTracks = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
    absT = cms.double(-1),
    absZ = cms.double(0.1),
    maxRecoT = cms.double(-1),
    maxRecoZ = cms.double(1000),
    sharedTrackFraction = cms.double(-1),
    sigmaT = cms.double(-1),
    sigmaZ = cms.double(3),
    trackAssociation = cms.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation")
)

hltPhase2PixelVertexAssociatorByPositionAndTracksWithMTD = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
    absT = cms.double(-1),
    absZ = cms.double(0.1),
    maxRecoT = cms.double(-1),
    maxRecoZ = cms.double(1000),
    sharedTrackFraction = cms.double(-1),
    sigmaT = cms.double(-1),
    sigmaZ = cms.double(3),
    trackAssociation = cms.InputTag("hltPhase2TrackingParticlePixelTrackExtendedWithMTDAsssociation")
)

hltPhase2TrackingParticlePixelTrackAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
    associator = cms.InputTag("quickTrackAssociatorByHits"),#PreSplitting"),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    label_tp = cms.InputTag("mix","MergedTrackTruth"),
    label_tr = cms.InputTag("hltPhase2PixelTracks")
)

hltPhase2TrackingParticlePixelTrackExtendedWithMTDAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
    associator = cms.InputTag("quickTrackAssociatorByHits"),#PreSplitting"),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    label_tp = cms.InputTag("mix","MergedTrackTruth"),
    label_tr = cms.InputTag("hltPixelTrackExtenderWithMTDBase")
)

hltPhase2TrackingParticleL1TrackAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
    associator = cms.InputTag("quickTrackAssociatorByHits"),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    label_tp = cms.InputTag("mix","MergedTrackTruth"),
    label_tr = cms.InputTag("hltPhase2L1CtfTracks"),
)

hltPhase2VertexAssociatorByPositionAndTracks = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
    absT = cms.double(-1),
    absZ = cms.double(0.1),
    maxRecoT = cms.double(-1),
    maxRecoZ = cms.double(1000),
    sharedTrackFraction = cms.double(-1),
    sigmaT = cms.double(-1),
    sigmaZ = cms.double(3),
    trackAssociation = cms.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation")
)

hltPhase2VertexAssociatorByPositionAndL1Tracks = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
    absT = cms.double(-1),
    absZ = cms.double(0.1),
    maxRecoT = cms.double(-1),
    maxRecoZ = cms.double(1000),
    sharedTrackFraction = cms.double(-1),
    sigmaT = cms.double(-1),
    sigmaZ = cms.double(3),
    trackAssociation = cms.InputTag("hltPhase2TrackingParticleL1TrackAsssociation")
)


hltPhase2CutsRecoTracksBtvLike = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(17.0),
    maxChi2 = cms.double(5.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(9),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(0),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(1), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-9),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(1.0),
    quality = cms.vstring(),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(0.2),
    usePV = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVHighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksFromPVHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVInitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVInitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksFromPVPt09Hp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksFromPVPt09InitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksFromPVPt09InitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), #previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('highPtTripletStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('highPtTripletStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
        vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('highPtTripletStep'),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(''),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('highPtTripletStep'),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksL1StepByOriginalAlgo  = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(''),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('hltIter0'),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring(''),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksL1StepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(""),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('hltIter0'),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksHighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring(),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #z("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksL1 = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('hltIter0'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring(),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksInitialStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('initialStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring(),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('initialStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('initialStep'),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring(),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring('initialStep'),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksInitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2L1CtfTracksPt09 = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(0), #3
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9),
    quality = cms.vstring(),
    src = cms.InputTag("hltPhase2L1CtfTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksL1Step = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(''),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(0), # 3?
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(2.0), # previous 0.1
    quality = cms.vstring(''), #'loose'),
    src = cms.InputTag("hltPhase2L1CtfTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksL1StepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(''),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(0), # 3?
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2L1CtfTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksPt09L1StepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(0), #3?
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2L1CtfTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksPt09HighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksPt09HighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksPt09Hp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksPt09InitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2CutsRecoTracksPt09InitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), #previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2GeneralTracksFromPV = cms.EDProducer("TrackWithVertexRefSelector",
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5),
    etaMin = cms.double(-5),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(1),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(0),
    ptErrorCut = cms.double(10000000000.0),
    maxOfValidPixelHits = cms.uint32(999),
    ptMax = cms.double(10000000000.0),
    ptMin = cms.double(0.9), # previous 0
    quality = cms.string('loose'),
    rhoVtx = cms.double(10000000000.0),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2PixelVertices"), #("hltPhase2OfflinePrimaryVertices"),
    vtxFallback = cms.bool(False),
    zetaVtx = cms.double(0.1)
)


hltPhase2GeneralTracksFromPVPt09 = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(0), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)


hltPhase2GeneralTracksPt09 = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0), minPixelLayer=cms.int32(4), maxPixelHit = cms.int32(99),
    minRapidity = cms.double(-4.5),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2OfflinePrimaryVertices")
)

hltPhase2SeedTrackshighPtTripletStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("hltPhase2HighPtTripletStepSeeds")
)


hltPhase2SeedTracksinitialStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("hltPhase2InitialStepSeeds")
)

hltPhase2TrackingParticleRecoTrackAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
    associator = cms.InputTag("quickTrackAssociatorByHits"),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    label_tp = cms.InputTag("mix","MergedTrackTruth"),
    label_tr = cms.InputTag("hltPhase2GeneralTracks")
)


hltPhase2TrackingParticlesElectron = cms.EDFilter("TrackingParticleRefSelector",
    chargedOnly = cms.bool(True),
    intimeOnly = cms.bool(False),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(100000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5), #10
    minHit = cms.int32(0),
    minPhi = cms.double(-3.2),
    minRapidity = cms.double(-4.5), #-10
    pdgId = cms.vint32(-11, 11),
    ptMax = cms.double(1e+100),
    ptMin = cms.double(0),
    signalOnly = cms.bool(False),
    src = cms.InputTag("mix","MergedTrackTruth"),
    stableOnly = cms.bool(False),
    tip = cms.double(100000.0)
)

hltPhase2TrackingParticlesSignal = cms.EDFilter("TrackingParticleRefSelector",
    chargedOnly = cms.bool(False),
    intimeOnly = cms.bool(False),
    invertRapidityCut = cms.bool(False), #cmssw_11_1
    lip = cms.double(100000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5), #10
    minHit = cms.int32(0),
    minPhi = cms.double(-3.2),
    minRapidity = cms.double(-4.5), #-10
    pdgId = cms.vint32(),
    ptMax = cms.double(1e+100),
    ptMin = cms.double(0),
    signalOnly = cms.bool(True),
    src = cms.InputTag("mix","MergedTrackTruth"),
    stableOnly = cms.bool(False),
    tip = cms.double(100000.0)
)

hltPhase2V0Validator = cms.EDProducer("V0Validator",
    DQMRootFileName = cms.untracked.string(''),
    dirName = cms.untracked.string('Vertexing/V0V'),
    kShortCollection = cms.untracked.InputTag("generalV0Candidates","Kshort"),
    lambdaCollection = cms.untracked.InputTag("generalV0Candidates","Lambda"),
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    vertexCollection = cms.untracked.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2SelectedOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2OfflinePrimaryVertices","","RECO") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2SelectedOfflinePrimaryVerticesWithBS = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2OfflinePrimaryVerticesWithBS")
)

hltPhase2SelectedPixelVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2PixelVertices")
)

hltPhase2VertexAnalysisTrackingOnly = cms.EDProducer("PrimaryVertexAnalyzer4PUSlimmed",
    do_generic_sim_plots = cms.untracked.bool(True),
    root_folder = cms.untracked.string('Vertexing/PrimaryVertexV'),
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    trackingParticleCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    use_only_charged_tracks = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks"),
    vertexRecoCollections = cms.VInputTag("hltPhase2OfflinePrimaryVertices", "hltPhase2OfflinePrimaryVerticesWithBS", "hltPhase2SelectedOfflinePrimaryVertices", "hltPhase2SelectedOfflinePrimaryVerticesWithBS")#, "hltPhase2FirstStepPrimaryVertices")
)

hltPhase2VertexAnalysisL1 = cms.EDProducer("PrimaryVertexAnalyzer4PUSlimmed",
    do_generic_sim_plots = cms.untracked.bool(True),
    root_folder = cms.untracked.string('Vertexing/PrimaryVertexV'),
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    trackingParticleCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    use_only_charged_tracks = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks"),
    vertexRecoCollections = cms.VInputTag("hltPhase2L1PrimaryVertex")#, "hltPhase2FirstStepPrimaryVertices")
)

hltPhase2PixelVertexAnalysisTrackingOnly = cms.EDProducer("PrimaryVertexAnalyzer4PUSlimmed",
    do_generic_sim_plots = cms.untracked.bool(False),
    root_folder = cms.untracked.string('Vertexing/PrimaryVertexV'),
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation"),
    trackingParticleCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    use_only_charged_tracks = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks"),
    vertexRecoCollections = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices")#,"hltPhase2TrimmedPixelVertices")#,"offlinePrimaryVertices")
)
