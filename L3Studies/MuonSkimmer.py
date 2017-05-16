import FWCore.ParameterSet.Config as cms

process = cms.Process( "BRSSkimmer" )

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
process.source = cms.Source( "PoolSource",fileNames = readFiles, secondaryFileNames = secFiles, inputCommands = cms.untracked.vstring('keep *'))

readFiles.extend( [
       '/store/relval/CMSSW_9_1_0_pre3/RelValZMM_13/MINIAODSIM/91X_upgrade2017_realistic_v3-v1/10000/2A61C7B9-A82F-E711-A6F4-0025905B8560.root',
] );
secFiles.extend( [
"/store/relval/CMSSW_9_1_0_pre3/RelValZMM_13/GEN-SIM-DIGI-RAW/91X_upgrade2017_realistic_v3-v1/10000/14676200-A02F-E711-8758-003048FFD76C.root",
"/store/relval/CMSSW_9_1_0_pre3/RelValZMM_13/GEN-SIM-DIGI-RAW/91X_upgrade2017_realistic_v3-v1/10000/56B6E630-A02F-E711-ADB6-003048FFD72C.root",
"/store/relval/CMSSW_9_1_0_pre3/RelValZMM_13/GEN-SIM-DIGI-RAW/91X_upgrade2017_realistic_v3-v1/10000/ACFFAE2C-A12F-E711-A485-0CC47A7C3404.root",
"/store/relval/CMSSW_9_1_0_pre3/RelValZMM_13/GEN-SIM-DIGI-RAW/91X_upgrade2017_realistic_v3-v1/10000/BED1DAAF-9F2F-E711-91FD-0CC47A7C3472.root",
#"/store/relval/CMSSW_9_1_0_pre3/RelValZMM_13/GEN-SIM-DIGI-RAW/91X_upgrade2017_realistic_v3-v1/10000/EE172B29-A12F-E711-A3B2-0CC47A4D7602.root"
] );

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.INFO.limit = 0
process.MessageLogger.cout.threshold = cms.untracked.string('WARNING')
process.MessageLogger.cerr.FwkSummary = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(100),
    limit = cms.untracked.int32(10000000)
)
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(100),
    limit = cms.untracked.int32(10000000)
)
process.maxEvents = cms.untracked.PSet(
       input = cms.untracked.int32( -1 )
#       input = cms.untracked.int32( 5000 )
)

process.hltOutputFULL = cms.OutputModule( "PoolOutputModule",
	fileName = cms.untracked.string( "ZMMRelval_1.root"),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string( '' ),
        filterName = cms.untracked.string( '' )
    ),
 #   SelectEvents = cms.untracked.PSet(
 #      SelectEvents = cms.vstring('pEF')
 #   ),
    outputCommands = cms.untracked.vstring(
#		'keep *',
		'drop *',
		'keep *_*Trigger*_*_*',
		'keep *_*Digi*_*_*',
		'keep *Muon*_*_*_*',
		'keep *Vertex*_*_*_*',
		'keep *_*hlt*_*_*',
		'keep *_rawDataCollector_*_*',
##		'keep recoMuons_muons_*_*',
#		'keep recoMuons_*_*_*',
#		'keep recoTracks_*_*_*',
#		'keep recoVertexs_*_*_*',
#		'keep *_*Trigger*_*_*',
#		'keep recoGenParticles_*_*_*'
    )
)

#process.EventFilter = cms.EDFilter('SelectEvents',
#        Filename = cms.string('EventsOfInterest.txt')
#)
#process.pEF = cms.Path(process.EventFilter)

process.outpath = cms.EndPath(process.hltOutputFULL)

process.options = cms.untracked.PSet(
	SkipEvent = cms.untracked.vstring('ProductNotFound')
)

