import FWCore.ParameterSet.Config as cms

process = cms.Process( "BRSSkimmer" )

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
process.source = cms.Source( "PoolSource",fileNames = readFiles, secondaryFileNames = secFiles, inputCommands = cms.untracked.vstring('keep *'))

readFiles.extend( [
       'root://xrootd-cms.infn.it//store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/0040ECBB-76EA-E611-8FE7-A0000420FE80.root'
] );
secFiles.extend( [
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/036/00000/BC5E1C50-789F-E611-9EC1-02163E01378B.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/036/00000/DAA09889-769F-E611-A97D-FA163E5C37B2.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/036/00000/4405C453-EA9E-E611-9BBD-02163E01209A.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/036/00000/D2FFD505-E99E-E611-B436-02163E011AE8.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/E0293396-7C9F-E611-A38D-02163E014155.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/ECCF1674-7C9F-E611-A4A7-02163E0133DD.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/8ABE4366-7B9F-E611-8001-02163E0121BE.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/985570B1-7C9F-E611-9C51-02163E011B59.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/24EDEF2F-839F-E611-B472-FA163E0776D6.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/F2FBD474-7C9F-E611-B678-FA163E62C748.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/1265698B-7A9F-E611-8201-02163E01349A.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/68C87C2D-849F-E611-8584-02163E01354D.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/3AA2BB43-839F-E611-848C-02163E0119C8.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/BCBF38B2-7A9F-E611-B4CD-02163E011BED.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/A8877257-839F-E611-B1DA-02163E0142B4.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/CCC9773B-7F9F-E611-A4AA-02163E0124D8.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/044F1877-7C9F-E611-8FA7-FA163E1EE921.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/AEEF8850-839F-E611-8A2E-02163E012835.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/123056B0-7A9F-E611-A174-FA163E1EE921.root",
"/store/data/Run2016H/SingleMuon/RAW/v1/000/284/037/00000/D63C6148-849F-E611-99B9-02163E01385A.root"
] );

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.INFO.limit = 0
process.MessageLogger.cout.threshold = cms.untracked.string('WARNING')
process.MessageLogger.cerr.FwkSummary = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(1000),
    limit = cms.untracked.int32(10000000)
)
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(1000),
    limit = cms.untracked.int32(10000000)
)
process.maxEvents = cms.untracked.PSet(
#       input = cms.untracked.int32( -1 )
       input = cms.untracked.int32( 5000 )
)

process.hltOutputFULL = cms.OutputModule( "PoolOutputModule",
	fileName = cms.untracked.string( "Data2016H_L2Fail.root"),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string( '' ),
        filterName = cms.untracked.string( '' )
    ),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring('pEF')
    ),
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

process.EventFilter = cms.EDFilter('SelectEvents',
        Filename = cms.string('EventsOfInterest.txt')
)
process.pEF = cms.Path(process.EventFilter)

process.outpath = cms.EndPath(process.hltOutputFULL)

process.options = cms.untracked.PSet(
	SkipEvent = cms.untracked.vstring('ProductNotFound')
)

