import numpy
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
#ZMM 80X:
files=[
"ZMMRelval_IterL3Out.root"
]

print "Running on ZMM:"
outName='Hist-20170512_ZMM91X_IterL3.root'
outputFile = TFile(outName,'RECREATE')

### Objects from file ###
muons, muonLabel = Handle("std::vector<pat::Muon>"), "slimmedMuons"
vertices, vertexLabel = Handle("std::vector<reco::Vertex>"), "offlineSlimmedPrimaryVertices"
triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","BRSHLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), ("selectedPatTriggerCustom","","BRSHLT")

### Histograms ###
allMuPt=TH1D("allMuPt","allMuPt",5000,0.0,5000.0)
allMuEta=TH1D("allMuEta","allMuEta",1000,-5.0,5.0)
allMuPhi=TH1D("allMuPhi","allMuPhi",800,-4.0,4.0)
passMuPt=TH1D("passMuPt","passMuPt",5000,0.0,5000.0)
passMuEta=TH1D("passMuEta","passMuEta",1000,-5.0,5.0)
passMuPhi=TH1D("passMuPhi","passMuPhi",800,-4.0,4.0)

dR=TH1D("dR","dR",1000,0.0,5.0)

numEvWL2=0
numEvWL3=0
### Events loop ###
count=0
for f in files:
	print "File: ",f
	events = Events(f)	#Use local
	for nEv,event in enumerate(events):
		count+=1
#		if count>=100: break
		if (count%5000==0): print "Event: ",count
		EventNum=str(event.eventAuxiliary().run())+":"+str(event.eventAuxiliary().luminosityBlock())+":"+str(event.eventAuxiliary().event())
		try:
			event.getByLabel(muonLabel,muons)
			event.getByLabel(vertexLabel, vertices)
			event.getByLabel(triggerBitLabel, triggerBits)
			event.getByLabel(triggerObjectLabel, triggerObjects)
		except RuntimeError:
			print "No muons/vertecies"
		if len(vertices.product()) == 0 or vertices.product()[0].ndof() < 4: continue
		else: PV = vertices.product()[0]

		### Muons ###
		numMuPassed=0
		selectedMuons=[]
		for i,mu in enumerate(muons.product()):
			if mu.pt() < 27 or not mu.isTightMuon(PV): continue #Looking at good muons
			numMuPassed+=1
			selectedMuons.append(mu)
		if verbose: print "number of muons passing selection in event: ",numMuPassed
		dRs=[]
		if (len(selectedMuons)>1):
#			for x in range(1,len(selectedMuons)):
#				dRs.append(dR.Fill(DeltaR2(selectedMuons[0],selectedMuons[xi])))
			if (DeltaR2(selectedMuons[0],selectedMuons[1])<0.6): continue

		#Iter L3:
		MuL1F = "hltL1fL1sMu22Or25L1Filtered0"			#Mu25
		MuL2F = "hltL2fL1sMu22Or25L1f0L2Filtered10Q"		#Mu25
		MuL3F = "hltL3fL1sMu22Or25L1f0L2f10QL3Filtered25Q"	#Mu25

		numL2=0
		numL3=0
		for mu in selectedMuons:
			allMu=False
			passMu=False
			for j,to in enumerate(triggerObjects.product()):
				if (DeltaR2(mu,to)<0.3):
					for f in to.filterLabels():
						if (f==MuL1F): allMu=True
						if (f==MuL3F): passMu=True
			if (allMu):
				numL2+=1
				numEvWL2+=1
				allMuPt.Fill(mu.pt())
				allMuEta.Fill(mu.eta())
				allMuPhi.Fill(mu.phi())
			if (passMu):
				numL3+=1
				numEvWL3+=1
				passMuPt.Fill(mu.pt())
				passMuEta.Fill(mu.eta())
				passMuPhi.Fill(mu.phi())
		if (numL3>numL2):
			print "More L3 than there are L2! ",EventNum
			print "numMu: ", numMuPassed
			for m,mu in enumerate(selectedMuons):
				print "mu [",m,"]: pt %6.2f eta %+5.3f phi %+5.3f " % (mu.pt(),mu.eta(),mu.phi())
				for j,to in enumerate(triggerObjects.product()):
					print "\tdR: ",DeltaR2(mu,to), ", ".join([str(f) for f in to.filterLabels()])," match?",("yes" if DeltaR2(mu,to)<0.3 else "no")
			print "DeltaR2(selectedMuons[0],selectedMuons[1]):",DeltaR2(selectedMuons[0],selectedMuons[1])
			for j,to in enumerate(triggerObjects.product()):
				for f in to.filterLabels():
					if (f==MuL2F): print "passed L2! Trigger object pt %6.2f eta %+5.3f phi %+5.3f " % (to.pt(),to.eta(),to.phi())
					if (f==MuL3F): print "passed L3! Trigger object pt %6.2f eta %+5.3f phi %+5.3f " % (to.pt(),to.eta(),to.phi())

outputFile.cd()

allMuPt.Write()
allMuEta.Write()
allMuPhi.Write()
passMuPt.Write()
passMuEta.Write()
passMuPhi.Write()
dR.Write()

outputFile.Close()
print count," events processed"
print "numEv with L2: ",numEvWL2
print "numEv with L3: ",numEvWL3

