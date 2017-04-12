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
files=[
"/store/relval/CMSSW_9_0_0/RelValTTbar_13/MINIAODSIM/90X_upgrade2017_realistic_v20_HS-v1/00000/10803548-3A15-E711-A0DF-0CC47A4D75F2.root",
"/store/relval/CMSSW_9_0_0/RelValTTbar_13/MINIAODSIM/90X_upgrade2017_realistic_v20_HS-v1/00000/9A82EB4B-3A15-E711-B3AB-0025905B857E.root",
"/store/relval/CMSSW_9_0_0/RelValTTbar_13/MINIAODSIM/90X_upgrade2017_realistic_v20_HS-v1/00000/9E26204C-3A15-E711-B349-0025905A497A.root"
]
print "Running on TTBar HS Plan1 sample:"
outName='Hist-20170412_TTbarPlan1.root'
outputFile = TFile(outName,'RECREATE')

### Objects from file ###
muons, muonLabel = Handle("std::vector<pat::Muon>"), "slimmedMuons"
vertices, vertexLabel = Handle("std::vector<reco::Vertex>"), "offlineSlimmedPrimaryVertices"
verticesScore = Handle("edm::ValueMap<float>")
triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "selectedPatTrigger"
gens, genLabel = Handle("vector<reco::GenParticle>"), "prunedGenParticles"

### Histograms ###
passedMu24Pt=TH1D("passedMu24Pt","passedMu24Pt",5000,0.0,5000.0)
passedMu24Eta=TH1D("passedMu24Eta","passedMu24Eta",1000,-5.0,5.0)
passedMu24Phi=TH1D("passedMu24Phi","passedMu24Phi",800,-4.0,4.0)
passedIsoMu24Pt=TH1D("passedIsoMu24Pt","passedIsoMu24Pt",5000,0.0,5000.0)
passedIsoMu24Eta=TH1D("passedIsoMu24Eta","passedIsoMu24Eta",1000,-5.0,5.0)
passedIsoMu24Phi=TH1D("passedIsoMu24Phi","passedIsoMu24Phi",800,-4.0,4.0)

passedEta1Mu24Pt=TH1D("passedEta1Mu24Pt","passedEta1Mu24Pt",5000,0.0,5000.0)
passedEta1Mu24Eta=TH1D("passedEta1Mu24Eta","passedEta1Mu24Eta",1000,-5.0,5.0)
passedEta1Mu24Phi=TH1D("passedEta1Mu24Phi","passedEta1Mu24Phi",800,-4.0,4.0)
passedEta1IsoMu24Pt=TH1D("passedEta1IsoMu24Pt","passedEta1IsoMu24Pt",5000,0.0,5000.0)
passedEta1IsoMu24Eta=TH1D("passedEta1IsoMu24Eta","passedEta1IsoMu24Eta",1000,-5.0,5.0)
passedEta1IsoMu24Phi=TH1D("passedEta1IsoMu24Phi","passedEta1IsoMu24Phi",800,-4.0,4.0)

passedEta2Mu24Pt=TH1D("passedEta2Mu24Pt","passedEta2Mu24Pt",5000,0.0,5000.0)
passedEta2Mu24Eta=TH1D("passedEta2Mu24Eta","passedEta2Mu24Eta",1000,-5.0,5.0)
passedEta2Mu24Phi=TH1D("passedEta2Mu24Phi","passedEta2Mu24Phi",800,-4.0,4.0)
passedEta2IsoMu24Pt=TH1D("passedEta2IsoMu24Pt","passedEta2IsoMu24Pt",5000,0.0,5000.0)
passedEta2IsoMu24Eta=TH1D("passedEta2IsoMu24Eta","passedEta2IsoMu24Eta",1000,-5.0,5.0)
passedEta2IsoMu24Phi=TH1D("passedEta2IsoMu24Phi","passedEta2IsoMu24Phi",800,-4.0,4.0)

passedEta3Mu24Pt=TH1D("passedEta3Mu24Pt","passedEta3Mu24Pt",5000,0.0,5000.0)
passedEta3Mu24Eta=TH1D("passedEta3Mu24Eta","passedEta3Mu24Eta",1000,-5.0,5.0)
passedEta3Mu24Phi=TH1D("passedEta3Mu24Phi","passedEta3Mu24Phi",800,-4.0,4.0)
passedEta3IsoMu24Pt=TH1D("passedEta3IsoMu24Pt","passedEta3IsoMu24Pt",5000,0.0,5000.0)
passedEta3IsoMu24Eta=TH1D("passedEta3IsoMu24Eta","passedEta3IsoMu24Eta",1000,-5.0,5.0)
passedEta3IsoMu24Phi=TH1D("passedEta3IsoMu24Phi","passedEta3IsoMu24Phi",800,-4.0,4.0)


### Events loop ###
count=0
for f in files:
	print "File: ",f
	events = Events(xrd+f)	#Use xrootd
#	events = Events(eos+f)	#Use eos
	for nEv,event in enumerate(events):
		count+=1
#		if count>=5000: break
		if (count%5000==0): print "Event: ",count
		EventNum=str(event.eventAuxiliary().run())+":"+str(event.eventAuxiliary().luminosityBlock())+":"+str(event.eventAuxiliary().event())
		try:
			event.getByLabel(muonLabel,muons)
			event.getByLabel(vertexLabel, vertices)
			event.getByLabel(vertexLabel, verticesScore)
			event.getByLabel(triggerBitLabel, triggerBits)
			event.getByLabel(triggerObjectLabel, triggerObjects)
			event.getByLabel(genLabel, gens)
		except RuntimeError:
			print "No muons/vertecies"
		if len(vertices.product()) == 0 or vertices.product()[0].ndof() < 4: continue
		else: PV = vertices.product()[0]

		### Muons ###
		numMuPassed=0
		selectedMuons=[]
		for i,mu in enumerate(muons.product()):
			if mu.pt() < 22 or not mu.isTightMuon(PV): continue #Looking at good muons
			if (mu.pfIsolationR04().sumChargedHadronPt + max(0., mu.pfIsolationR04().sumNeutralHadronEt + mu.pfIsolationR04().sumPhotonEt - 0.5*mu.pfIsolationR04().sumPUPt))/mu.pt() >0.15: continue #PFIso tight=0.15, loose=0.25
			numMuPassed+=1
			selectedMuons.append(mu)
		if verbose: print "number of muons passing selection in event: ",numMuPassed
        
        	### Trigger ###
		isoMu20RF = "hltL3fL1sMu18L1f0L2f10QL3Filtered20Q" #IsoMu20 reco filter
		isoMu20IF = "hltL3crIsoL1sMu18L1f0L2f10QL3f20QL3trkIsoFiltered0p09" #IsoMu20 isolation filter
		isoTkMu20RF = "hltL3fL1sMu18f0TkFiltered20Q" #IsoTkMu20 reco filter
		isoTkMu20IF = "hltL3fL1sMu18L1f0Tkf20QL3trkIsoFiltered0p09" #IsoTkMu20 isolation filter
		isoMu24RF = "hltL3fL1sMu22L1f0L2f10QL3Filtered24Q" #IsoMu24 reco filter
		isoMu24IF = "hltL3crIsoL1sMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p09" #IsoMu24 isolation filter

		names = event.object().triggerNames(triggerBits.product())
		for j,to in enumerate(triggerObjects.product()):
			for f in to.filterLabels():
				if (f==isoMu20RF or f==isoTkMu20RF):
#					print "passed (Tk)Mu20! Trigger object pt %6.2f eta %+5.3f phi %+5.3f " % (to.pt(),to.eta(),to.phi())
					for mu in selectedMuons:
						if (DeltaR2(mu,to)<0.2):
							passedMu24Pt.Fill(mu.pt())
							passedMu24Eta.Fill(mu.eta())
							passedMu24Phi.Fill(mu.phi())
							if (mu.eta()<-1.3):
								passedEta1Mu24Pt.Fill(mu.pt())
								passedEta1Mu24Eta.Fill(mu.eta())
								passedEta1Mu24Phi.Fill(mu.phi())
							if (mu.eta()<1.3 and mu.eta()>-1.3):
								passedEta2Mu24Pt.Fill(mu.pt())
								passedEta2Mu24Eta.Fill(mu.eta())
								passedEta2Mu24Phi.Fill(mu.phi())
							if (mu.eta()>1.3):
								passedEta3Mu24Pt.Fill(mu.pt())
								passedEta3Mu24Eta.Fill(mu.eta())
								passedEta3Mu24Phi.Fill(mu.phi())

				if (f==isoMu20IF or f==isoTkMu20IF):
#					print "passed Iso(Tk)Mu20! Trigger object pt %6.2f eta %+5.3f phi %+5.3f " % (to.pt(),to.eta(),to.phi())
					for mu in selectedMuons:
						if (DeltaR2(mu,to)<0.2):
							passedIsoMu24Pt.Fill(mu.pt())
							passedIsoMu24Eta.Fill(mu.eta())
							passedIsoMu24Phi.Fill(mu.phi())
							if (mu.eta()<-1.3):
								passedEta1IsoMu24Pt.Fill(mu.pt())
								passedEta1IsoMu24Eta.Fill(mu.eta())
								passedEta1IsoMu24Phi.Fill(mu.phi())
							if (mu.eta()<1.3 and mu.eta()>-1.3):
								passedEta2IsoMu24Pt.Fill(mu.pt())
								passedEta2IsoMu24Eta.Fill(mu.eta())
								passedEta2IsoMu24Phi.Fill(mu.phi())
							if (mu.eta()>1.3):
								passedEta3IsoMu24Pt.Fill(mu.pt())
								passedEta3IsoMu24Eta.Fill(mu.eta())
								passedEta3IsoMu24Phi.Fill(mu.phi())


outputFile.cd()

passedMu24Pt.Write()
passedMu24Eta.Write()
passedMu24Phi.Write()
passedIsoMu24Pt.Write()
passedIsoMu24Eta.Write()
passedIsoMu24Phi.Write()

passedEta1Mu24Pt.Write()
passedEta1Mu24Eta.Write()
passedEta1Mu24Phi.Write()
passedEta1IsoMu24Pt.Write()
passedEta1IsoMu24Eta.Write()
passedEta1IsoMu24Phi.Write()

passedEta2Mu24Pt.Write()
passedEta2Mu24Eta.Write()
passedEta2Mu24Phi.Write()
passedEta2IsoMu24Pt.Write()
passedEta2IsoMu24Eta.Write()
passedEta2IsoMu24Phi.Write()

passedEta3Mu24Pt.Write()
passedEta3Mu24Eta.Write()
passedEta3Mu24Phi.Write()
passedEta3IsoMu24Pt.Write()
passedEta3IsoMu24Eta.Write()
passedEta3IsoMu24Phi.Write()

outputFile.Close()
print count," events processed"

