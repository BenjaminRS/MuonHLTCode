from hlt import *

process.source.fileNames=cms.untracked.vstring(
	'file:ZMMRelval_1.root',
	'file:ZMMRelval_2.root'
)

process.maxEvents.input = cms.untracked.int32(-1)

process.hltOutputFULL = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "ZMMRelval_IterL3Out.root"),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string( '' ),
        filterName = cms.untracked.string( '' )
    ),
    outputCommands = cms.untracked.vstring(
                'drop *',
                'keep *_*Trigger*_*_BRSHLT',
		'keep *_selectedPatTrigger_*_*',
                'keep *Muon*_slimmedMuons_*_RECO',
                'keep *Vertex*_offlineSlimmedPrimaryVertices_*_*',
#                'keep *_*hlt*_*_*',
    )
)

#From Riccardo
process_name = process.name_()
process.patTriggerCustom = cms.EDProducer(
    'PATTriggerProducer',
    TriggerResults              = cms.InputTag('TriggerResults'      , '', process_name),
    hltTriggerSummaryAOD        = cms.InputTag('hltTriggerSummaryAOD', '', process_name),
    l1tAlgBlkInputTag           = cms.InputTag('hltgtStage2Digis'    , '', process_name),
    l1tExtBlkInputTag           = cms.InputTag('hltgtStage2Digis'    , '', process_name),
    onlyStandAlone              = cms.bool(True),
    packTriggerPathNames        = cms.bool(True),
    processName                 = cms.string(process_name)
)

process.selectedPatTriggerCustom = cms.EDFilter(
    'PATTriggerObjectStandAloneSelector',
    cut = cms.string('!filterLabels.empty()'),
    src = cms.InputTag('patTriggerCustom')
)

if not hasattr(process, 'HLTPatTrig'):
	print 'added needed endpath'
	process.HLTPatTrig = cms.EndPath(process.patTriggerCustom * process.selectedPatTriggerCustom)
	process.HLTSchedule.append(process.HLTPatTrig)
else:
	process.HLTPatTrig += process.patTriggerCustom
	process.HLTPatTrig += process.selectedPatTriggerCustom


#from PhysicsTools.PatAlgos.tools.trigTools import * 
#switchOnTriggerStandAlone(
#    process,
#     path            = 'outpath',
##    path            = 'HLTAnalyzerEndpath',
#    triggerProducer = 'patTriggerCustom',
#    hltProcess      = '*',
#    outputModule    = 'hltOutputFULL'
##     triggerResults
##     triggerEvent
#)
#process.patTriggerCustomBRS = cms.EDProducer('PATTriggerProducer',
#    l1GtReadoutRecordInputTag = cms.InputTag('gtDigis'),
#    l1GtRecordInputTag = cms.InputTag('gtDigis'),
#    l1GtTriggerMenuLiteInputTag = cms.InputTag('gtDigis'),
#    onlyStandAlone = cms.bool(True),
#    processName = cms.string('TEST')
#)
#switchOnTrigger( process, path = 'outpath', triggerProducer = 'patTriggerCustomBRS', hltProcess = '*', outputModule = 'hltOutputFULL')
#switchOnTrigger( process, hltProcess = 'BRSHLT', outputModule = 'hltOutputFULL')

process.outpath = cms.EndPath(process.hltOutputFULL)


