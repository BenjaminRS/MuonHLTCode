import ROOT
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()
from DataFormats.FWLite import Events, Handle
from ROOT import TVector3,TLorentzVector,TFile,TH1D,TRandom3
DeltaR = ROOT.Math.VectorUtil.DeltaR
DeltaPhi = ROOT.Math.VectorUtil.DeltaPhi
DeltaR2 = lambda a, b: DeltaR(a.p4(), b.p4())       # for reco::Candidates
DeltaPhi2 = lambda a, b: DeltaPhi(a.p4(), b.p4())   # for reco::Candidates

verbose=False
#verbose=True

### IO ###
xrd="root://xrootd-cms.infn.it/"
eos="/afs/cern.ch/user/b/benjamin/eos/cms"
files=[
"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/0040ECBB-76EA-E611-8FE7-A0000420FE80.root"
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/16F28614-84EA-E611-8083-A0369F310374.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/26C54321-7DEA-E611-97EC-B8CA3A70A5E8.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/36F116DC-8AEA-E611-84D5-24BE05C62711.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/40222852-7DEA-E611-9290-A0369F310374.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/42282F9B-75EA-E611-A0D2-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/4C3A6DE3-7DEA-E611-8664-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/520C6456-7DEA-E611-B733-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/52C02EA9-7EEA-E611-BA67-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/62689638-84EA-E611-BD20-B8CA3A70BAC8.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/70A3D0A6-7EEA-E611-BD71-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/7C6611B8-76EA-E611-8644-24BE05C636E1.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/88639E52-7DEA-E611-9102-A0369F310374.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/88EECBB2-91EA-E611-8C21-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/9620E3D8-7DEA-E611-BF13-24BE05C6E7C1.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/9C332DDA-7DEA-E611-8821-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/A606F1A0-75EA-E611-814B-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/AAE018B8-76EA-E611-A676-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/AAE662B8-76EA-E611-811A-5065F381A2F1.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/B4FAEA51-7DEA-E611-9BB6-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/B80050BC-76EA-E611-B0B0-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/BAAAA854-84EA-E611-9A52-B8CA3A70BAC8.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/C04E3FBD-76EA-E611-AA2F-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/C6CF8076-8BEA-E611-94E0-24BE05CE3C91.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/CE0D2338-7DEA-E611-A8F7-A0369F310374.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/CE40C7B7-76EA-E611-BD9F-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/DC5FA286-7CEA-E611-982C-B8CA3A70A5E8.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/E2FBF0A1-84EA-E611-8A3F-002590D9D9F0.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/F001FEB6-76EA-E611-A1C3-A0000420FE80.root",
#"/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/F0B09550-7DEA-E611-A445-B8CA3A70A5E8.root"
]
fout = open('EventsOfInterest.txt', 'w')

### Objects from file ###
triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "selectedPatTrigger"

### Events loop ###
numL1=0
numL2=0
numEvWL1=0
numEvWL2=0
count=0
for f in files:
	print "File: ",f
	events = Events(xrd+f)	#Use xrootd
#	events = Events(eos+f)	#Use eos
	for nEv,event in enumerate(events):
		count+=1
		foundL1=False
		foundL2=False
#		if count>=500: break
		if (count%5000==0): print "Event: ",count
		EventNum=str(event.eventAuxiliary().run())+":"+str(event.eventAuxiliary().luminosityBlock())+":"+str(event.eventAuxiliary().event())
		try:
			event.getByLabel(triggerBitLabel, triggerBits)
			event.getByLabel(triggerObjectLabel, triggerObjects)
		except RuntimeError:
			print "No trigger info"
		
        	### Trigger ###
		l1f = "hltL1fL1sMu22L1Filtered0"	#L1 muon for IsoMu24 and IsoTkMu24
		l2f = "hltL2fL1sMu22L1f0L2Filtered10Q"	#L2 muon for IsoMu24
		names = event.object().triggerNames(triggerBits.product())
		for j,to in enumerate(triggerObjects.product()):
			for f in to.filterLabels():
				if (f==l1f):
#					print "found L1! Trigger object pt %6.2f eta %+5.3f phi %+5.3f " % (to.pt(),to.eta(),to.phi())
					numL1+=1
					foundL1=True
				if (f==l2f):
#                                       print "found L2! Trigger object pt %6.2f eta %+5.3f phi %+5.3f " % (to.pt(),to.eta(),to.phi())
                                        numL2+=1
					foundL2=True
		if foundL1: numEvWL1+=1
		if foundL2: numEvWL2+=1
		if foundL1 and not foundL2: fout.write(EventNum+'\n')
print count," events processed"
print "numEv with L1: ",numEvWL1
print "numEv with L2: ",numEvWL2
print "tot numL1: ",numL1
print "tot numL2: ",numL2


