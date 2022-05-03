from dqm_modules import *
import FWCore.ParameterSet.Config as cms
from DQMOffline.Configuration.DQMOfflineMC_cff import *

dqm_commons = cms.Task(TrackSplitMonitor,dqmInfoTracking)

dqm_commons_offline = cms.Task(TrackSplitMonitor,dqmInfoTracking)

dqm_initial = cms.Task(hltPhase2TrackSeedMoninitialStep)

dqm_highpt = cms.Task(hltPhase2TrackSeedMonhighPtTripletStep)

dqm_vertex = cms.Task(hltPhase2PvMonitor,hltPhase2PrimaryVertexResolution,hltPhase2TrackingDQMgoodOfflinePrimaryVertices)

dqm_pixelvertex = cms.Task(hltPhase2TrackingDQMgoodPixelVertices,hltPhase2TrackingDQMgoodPixelVertices)

dqm_general = cms.Task(hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks,
                       ##High Purity & Selectors
                       hltPhase2PV0p1, hltPhase2HighPurityPV0p1, #PV
                       hltPhase2HighPurityPt1,hltPhase2HighPurityPtRange0to1, #PT
                       #Monitors
                       hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPV0p1,
                       hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPt1,
                       hltPhase2TrackerCollisionSelectedTrackMonCommonhighPurityPtRange0to1,
                       #Eff Mon
                       hltPhase2TrackMon_ckf)

dqm_l1 = cms.Task()

dqm_original = cms.EndPath(dqm_commons,dqm_vertex,dqm_pixelvertex,dqm_initial,dqm_highpt,dqm_general)
dqm_l1initial = cms.EndPath(dqm_commons,dqm_vertex,dqm_pixelvertex,dqm_initial,dqm_general)
dqm_l1trip = cms.EndPath(dqm_commons,dqm_vertex,dqm_pixelvertex,dqm_highpt,dqm_general)
dqm_base= cms.EndPath(dqm_commons)
dqm_onestep =  cms.EndPath(dqm_commons,dqm_vertex,dqm_pixelvertex,dqm_initial,dqm_general)
dqm_pixel = cms.EndPath(dqm_commons,dqm_pixelvertex)
dqm_all = cms.EndPath(dqm_commons,dqm_vertex,dqm_pixelvertex,dqm_initial,dqm_highpt,dqm_general)
dqm_pixelMTD = cms.EndPath(dqm_pixelvertex)
