import numpy
import ROOT
from ROOT import *

### Macros ###
def plot(canvas,name):
    canvas.Print(name+".pdf","pdf")
#    canvas.Print(name+".png","png")
#    canvas.Print(name+".eps","eps")

def setStyle(hist,value):
    hist.SetLineColor(value)
    hist.SetMarkerColor(value)
    hist.SetMarkerStyle(20)
    hist.SetMarkerSize(0.8)

### Binning ###
PtBins=numpy.array([0.0, 20.0, 22.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 125.0, 150.0, 200.0, 400.0])
nPtBins=len(PtBins)-1

EtaBins=numpy.array([-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4])
nEtaBins=len(EtaBins)-1

pi=3.14
PhiBins=numpy.array([-pi,-(11.0/12.0)*pi,-(9.0/12.0)*pi,-(7.0/12.0)*pi,-(5.0/12.0)*pi,-(3.0/12.0)*pi,-(1.0/12.0)*pi,(1.0/12.0)*pi,(3.0/12.0)*pi,(5.0/12.0)*pi,(7.0/12.0)*pi,(9.0/12.0)*pi,(11.0/12.0)*pi,pi])
nPhiBins=len(PhiBins)-1

### Style ###
gStyle.SetOptStat("")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

### IO ###
f=ROOT.TFile("Hist-20170412_TTbarPlan1.root")


########################################################################

######## Eff Vs Muon Pt ########
cPt = TCanvas("cPt", "cPt", 700, 700)
cPt.SetLeftMargin(0.12)
cPt.SetBottomMargin(0.12)
cPt.SetRightMargin(0.08);
cPt.SetTopMargin(0.08);

f.cd()
all24Pt = passedMu24Pt.Clone()
print "Pass Mu24: ",all24Pt.GetEntries()
pass24Pt = passedIsoMu24Pt.Clone()
print "Pass IsoMu24: ",pass24Pt.GetEntries()
all24Pt.Rebin(nPtBins,"All24Pt",PtBins)
pass24Pt.Rebin(nPtBins,"Pass24Pt",PtBins)
Ptall24=ROOT.gDirectory.Get("All24Pt")
dPtAll24=ROOT.TH1D(Ptall24)
Ptpass24=ROOT.gDirectory.Get("Pass24Pt")
nPtPass24=ROOT.TH1D(Ptpass24)

effPt = ROOT.TEfficiency(nPtPass24,dPtAll24)
effPt.SetTitle(";Muon p_{T} (GeV);Isolation Efficiency")
setStyle(effPt,1)
effPt.Draw("")
effPt.Paint("")
effPt.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPt.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
#effPt.GetPaintedGraph().GetYaxis().SetRangeUser(0.9,1.0)
effPt.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)

plot(cPt,"IsoEffVsPt")
#effPt.GetPaintedGraph().GetYaxis().SetRangeUser(0.7,0.95)
#plot(cPt,"IsoEffVsPt_zoom")


######## Eff Vs Muon Pt1 ########
cPt1 = TCanvas("cPt1", "cPt1", 700, 700)
cPt1.SetLeftMargin(0.12)
cPt1.SetBottomMargin(0.12)
cPt1.SetRightMargin(0.08);
cPt1.SetTopMargin(0.08);

f.cd()
all24Pt1 = passedEta1Mu24Pt.Clone()
print "Pass Mu24: ",all24Pt1.GetEntries()
pass24Pt1 = passedEta1IsoMu24Pt.Clone()
print "Pass IsoMu24: ",pass24Pt1.GetEntries()
all24Pt1.Rebin(nPtBins,"All24Pt1",PtBins)
pass24Pt1.Rebin(nPtBins,"Pass24Pt1",PtBins)
Pt1all24=ROOT.gDirectory.Get("All24Pt1")
dPt1All24=ROOT.TH1D(Pt1all24)
Pt1pass24=ROOT.gDirectory.Get("Pass24Pt1")
nPt1Pass24=ROOT.TH1D(Pt1pass24)

effPt1 = ROOT.TEfficiency(nPt1Pass24,dPt1All24)
effPt1.SetTitle(";Muon p_{T} (GeV);Isolation Efficiency")
setStyle(effPt1,1)
effPt1.Draw("")
effPt1.Paint("")
effPt1.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPt1.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
#effPt1.GetPaintedGraph().GetYaxis().SetRangeUser(0.9,1.0)
effPt1.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)

plot(cPt1,"IsoEffVsPt1")
#effPt1.GetPaintedGraph().GetYaxis().SetRangeUser(0.7,0.95)
#plot(cPt1,"IsoEffVsPt1_zoom")


######## Eff Vs Muon Pt2 ########
cPt2 = TCanvas("cPt2", "cPt2", 700, 700)
cPt2.SetLeftMargin(0.12)
cPt2.SetBottomMargin(0.12)
cPt2.SetRightMargin(0.08);
cPt2.SetTopMargin(0.08);

f.cd()
all24Pt2 = passedEta2Mu24Pt.Clone()
print "Pass Mu24: ",all24Pt2.GetEntries()
pass24Pt2 = passedEta2IsoMu24Pt.Clone()
print "Pass IsoMu24: ",pass24Pt2.GetEntries()
all24Pt2.Rebin(nPtBins,"All24Pt2",PtBins)
pass24Pt2.Rebin(nPtBins,"Pass24Pt2",PtBins)
Pt2all24=ROOT.gDirectory.Get("All24Pt2")
dPt2All24=ROOT.TH1D(Pt2all24)
Pt2pass24=ROOT.gDirectory.Get("Pass24Pt2")
nPt2Pass24=ROOT.TH1D(Pt2pass24)

effPt2 = ROOT.TEfficiency(nPt2Pass24,dPt2All24)
effPt2.SetTitle(";Muon p_{T} (GeV);Isolation Efficiency")
setStyle(effPt2,1)
effPt2.Draw("")
effPt2.Paint("")
effPt2.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPt2.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
#effPt2.GetPaintedGraph().GetYaxis().SetRangeUser(0.9,1.0)
effPt2.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)

plot(cPt2,"IsoEffVsPt2")
#effPt2.GetPaintedGraph().GetYaxis().SetRangeUser(0.7,0.95)
#plot(cPt2,"IsoEffVsPt2_zoom")


######## Eff Vs Muon Pt3 ########
cPt3 = TCanvas("cPt3", "cPt3", 700, 700)
cPt3.SetLeftMargin(0.12)
cPt3.SetBottomMargin(0.12)
cPt3.SetRightMargin(0.08);
cPt3.SetTopMargin(0.08);

f.cd()
all24Pt3 = passedEta3Mu24Pt.Clone()
print "Pass Mu24: ",all24Pt3.GetEntries()
pass24Pt3 = passedEta3IsoMu24Pt.Clone()
print "Pass IsoMu24: ",pass24Pt3.GetEntries()
all24Pt3.Rebin(nPtBins,"All24Pt3",PtBins)
pass24Pt3.Rebin(nPtBins,"Pass24Pt3",PtBins)
Pt3all24=ROOT.gDirectory.Get("All24Pt3")
dPt3All24=ROOT.TH1D(Pt3all24)
Pt3pass24=ROOT.gDirectory.Get("Pass24Pt3")
nPt3Pass24=ROOT.TH1D(Pt3pass24)

effPt3 = ROOT.TEfficiency(nPt3Pass24,dPt3All24)
effPt3.SetTitle(";Muon p_{T} (GeV);Isolation Efficiency")
setStyle(effPt3,1)
effPt3.Draw("")
effPt3.Paint("")
effPt3.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPt3.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
#effPt3.GetPaintedGraph().GetYaxis().SetRangeUser(0.9,1.0)
effPt3.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)

plot(cPt3,"IsoEffVsPt3")
#effPt3.GetPaintedGraph().GetYaxis().SetRangeUser(0.7,0.95)
#plot(cPt3,"IsoEffVsPt3_zoom")


########################################################################

######## Eff Vs Muon Eta ########
cEta = TCanvas("cEta", "cEta", 700, 700)
cEta.SetLeftMargin(0.12)
cEta.SetBottomMargin(0.12)
cEta.SetRightMargin(0.08);
cEta.SetTopMargin(0.08);

f.cd()
all24Eta = passedMu24Eta.Clone()
print "Pass Mu24: ",all24Eta.GetEntries()
pass24Eta = passedIsoMu24Eta.Clone()
print "Pass IsoMu24: ",pass24Eta.GetEntries()
all24Eta.Rebin(nEtaBins,"All24Eta",EtaBins)
pass24Eta.Rebin(nEtaBins,"Pass24Eta",EtaBins)
Etaall24=ROOT.gDirectory.Get("All24Eta")
dEtaAll24=ROOT.TH1D(Etaall24)
Etapass24=ROOT.gDirectory.Get("Pass24Eta")
nEtaPass24=ROOT.TH1D(Etapass24)

effEta = ROOT.TEfficiency(nEtaPass24,dEtaAll24)
effEta.SetTitle(";Muon #eta;Isolation Efficiency")
setStyle(effEta,1)
effEta.Draw("")
effEta.Paint("")
effEta.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effEta.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
effEta.GetPaintedGraph().GetXaxis().SetRangeUser(-2.8,2.8)
effEta.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)

plot(cEta,"IsoEffVsEta")

#Change eta binning as the plots are now split into -2.4,-1.3,1.3,2.4
EtaBins=numpy.array([-2.4,-2.1,-1.6,-1.3,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.3,1.6,2.1,2.4])
nEtaBins=len(EtaBins)-1


######## Eff Vs Muon Eta1 ########
cEta1 = TCanvas("cEta1", "cEta1", 700, 700)
cEta1.SetLeftMargin(0.12)
cEta1.SetBottomMargin(0.12)
cEta1.SetRightMargin(0.08);
cEta1.SetTopMargin(0.08);

f.cd()
all24Eta1 = passedEta1Mu24Eta.Clone()
print "Pass Mu24: ",all24Eta1.GetEntries()
pass24Eta1 = passedEta1IsoMu24Eta.Clone()
print "Pass IsoMu24: ",pass24Eta1.GetEntries()
all24Eta1.Rebin(nEtaBins,"All24Eta1",EtaBins)
pass24Eta1.Rebin(nEtaBins,"Pass24Eta1",EtaBins)
Eta1all24=ROOT.gDirectory.Get("All24Eta1")
dEta1All24=ROOT.TH1D(Eta1all24)
Eta1pass24=ROOT.gDirectory.Get("Pass24Eta1")
nEta1Pass24=ROOT.TH1D(Eta1pass24)

effEta1 = ROOT.TEfficiency(nEta1Pass24,dEta1All24)
effEta1.SetTitle(";Muon #eta;Isolation Efficiency")
setStyle(effEta1,1)
effEta1.Draw("")
effEta1.Paint("")
effEta1.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effEta1.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
effEta1.GetPaintedGraph().GetXaxis().SetRangeUser(-2.8,2.8)
effEta1.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)
plot(cEta1,"IsoEffVsEta1")


######## Eff Vs Muon Eta2 ########
cEta2 = TCanvas("cEta2", "cEta2", 700, 700)
cEta2.SetLeftMargin(0.12)
cEta2.SetBottomMargin(0.12)
cEta2.SetRightMargin(0.08);
cEta2.SetTopMargin(0.08);

f.cd()
all24Eta2 = passedEta2Mu24Eta.Clone()
print "Pass Mu24: ",all24Eta2.GetEntries()
pass24Eta2 = passedEta2IsoMu24Eta.Clone()
print "Pass IsoMu24: ",pass24Eta2.GetEntries()
all24Eta2.Rebin(nEtaBins,"All24Eta2",EtaBins)
pass24Eta2.Rebin(nEtaBins,"Pass24Eta2",EtaBins)
Eta2all24=ROOT.gDirectory.Get("All24Eta2")
dEta2All24=ROOT.TH1D(Eta2all24)
Eta2pass24=ROOT.gDirectory.Get("Pass24Eta2")
nEta2Pass24=ROOT.TH1D(Eta2pass24)

effEta2 = ROOT.TEfficiency(nEta2Pass24,dEta2All24)
effEta2.SetTitle(";Muon #eta;Isolation Efficiency")
setStyle(effEta2,1)
effEta2.Draw("")
effEta2.Paint("")
effEta2.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effEta2.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
effEta2.GetPaintedGraph().GetXaxis().SetRangeUser(-2.8,2.8)
effEta2.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)

plot(cEta2,"IsoEffVsEta2")


######## Eff Vs Muon Eta3 ########
cEta3 = TCanvas("cEta3", "cEta3", 700, 700)
cEta3.SetLeftMargin(0.12)
cEta3.SetBottomMargin(0.12)
cEta3.SetRightMargin(0.08);
cEta3.SetTopMargin(0.08);

f.cd()
all24Eta3 = passedEta3Mu24Eta.Clone()
print "Pass Mu24: ",all24Eta3.GetEntries()
pass24Eta3 = passedEta3IsoMu24Eta.Clone()
print "Pass IsoMu24: ",pass24Eta3.GetEntries()
all24Eta3.Rebin(nEtaBins,"All24Eta3",EtaBins)
pass24Eta3.Rebin(nEtaBins,"Pass24Eta3",EtaBins)
Eta3all24=ROOT.gDirectory.Get("All24Eta3")
dEta3All24=ROOT.TH1D(Eta3all24)
Eta3pass24=ROOT.gDirectory.Get("Pass24Eta3")
nEta3Pass24=ROOT.TH1D(Eta3pass24)

effEta3 = ROOT.TEfficiency(nEta3Pass24,dEta3All24)
effEta3.SetTitle(";Muon #eta;Isolation Efficiency")
setStyle(effEta3,1)
effEta3.Draw("")
effEta3.Paint("")
effEta3.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effEta3.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
effEta3.GetPaintedGraph().GetXaxis().SetRangeUser(-2.8,2.8)
effEta3.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)

plot(cEta3,"IsoEffVsEta3")


########################################################################

######## Eff Vs Muon Phi ########
cPhi = TCanvas("cPhi", "cPhi", 700, 700)
cPhi.SetLeftMargin(0.12)
cPhi.SetBottomMargin(0.12)
cPhi.SetRightMargin(0.08);
cPhi.SetTopMargin(0.08);

f.cd()
all24Phi = passedMu24Phi.Clone()
print "Pass Mu24: ",all24Phi.GetEntries()
pass24Phi = passedIsoMu24Phi.Clone()
print "Pass IsoMu24: ",pass24Phi.GetEntries()

all24Phi.Rebin(nPhiBins,"All24Phi",PhiBins)
pass24Phi.Rebin(nPhiBins,"Pass24Phi",PhiBins)

Phiall24=ROOT.gDirectory.Get("All24Phi")
dPhiAll24=ROOT.TH1D(Phiall24)
Phipass24=ROOT.gDirectory.Get("Pass24Phi")
nPhiPass24=ROOT.TH1D(Phipass24)

effPhi = ROOT.TEfficiency(nPhiPass24,dPhiAll24)
effPhi.SetTitle(";Muon #phi;Isolation Efficiency")
setStyle(effPhi,1)
effPhi.Draw("")
effPhi.Paint("")
effPhi.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPhi.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
effPhi.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)
#effPhi.GetPaintedGraph().GetYaxis().SetRangeUser(0.6,1.0)

plot(cPhi,"IsoEffVsPhi")

#Change phi binning after the plots are now split into eta=-2.4,-1.3,1.3,2.4
PhiBins=numpy.array([-pi,-2.5,-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0,2.5,pi])
nPhiBins=len(PhiBins)-1

######## Eff Vs Muon Phi1 ########
cPhi1 = TCanvas("cPhi1", "cPhi1", 700, 700)
cPhi1.SetLeftMargin(0.12)
cPhi1.SetBottomMargin(0.12)
cPhi1.SetRightMargin(0.08);
cPhi1.SetTopMargin(0.08);

f.cd()
all24Phi1 = passedEta1Mu24Phi.Clone()
print "Pass Mu24: ",all24Phi1.GetEntries()
pass24Phi1 = passedEta1IsoMu24Phi.Clone()
print "Pass IsoMu24: ",pass24Phi1.GetEntries()

all24Phi1.Rebin(nPhiBins,"All24Phi1",PhiBins)
pass24Phi1.Rebin(nPhiBins,"Pass24Phi1",PhiBins)

Phi1all24=ROOT.gDirectory.Get("All24Phi1")
dPhi1All24=ROOT.TH1D(Phi1all24)
Phi1pass24=ROOT.gDirectory.Get("Pass24Phi1")
nPhi1Pass24=ROOT.TH1D(Phi1pass24)

effPhi1 = ROOT.TEfficiency(nPhi1Pass24,dPhi1All24)
effPhi1.SetTitle(";Muon #phi;Isolation Efficiency")
setStyle(effPhi1,1)
effPhi1.Draw("")
effPhi1.Paint("")
effPhi1.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPhi1.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
effPhi1.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)
#effPhi1.GetPaintedGraph().GetYaxis().SetRangeUser(0.6,1.0)

plot(cPhi1,"IsoEffVsPhi1")


######## Eff Vs Muon Phi2 ########
cPhi2 = TCanvas("cPhi2", "cPhi2", 700, 700)
cPhi2.SetLeftMargin(0.12)
cPhi2.SetBottomMargin(0.12)
cPhi2.SetRightMargin(0.08);
cPhi2.SetTopMargin(0.08);

f.cd()
all24Phi2 = passedEta2Mu24Phi.Clone()
print "Pass Mu24: ",all24Phi2.GetEntries()
pass24Phi2 = passedEta2IsoMu24Phi.Clone()
print "Pass IsoMu24: ",pass24Phi2.GetEntries()

all24Phi2.Rebin(nPhiBins,"All24Phi2",PhiBins)
pass24Phi2.Rebin(nPhiBins,"Pass24Phi2",PhiBins)

Phi2all24=ROOT.gDirectory.Get("All24Phi2")
dPhi2All24=ROOT.TH1D(Phi2all24)
Phi2pass24=ROOT.gDirectory.Get("Pass24Phi2")
nPhi2Pass24=ROOT.TH1D(Phi2pass24)

effPhi2 = ROOT.TEfficiency(nPhi2Pass24,dPhi2All24)
effPhi2.SetTitle(";Muon #phi;Isolation Efficiency")
setStyle(effPhi2,1)
effPhi2.Draw("")
effPhi2.Paint("")
effPhi2.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPhi2.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
effPhi2.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)
#effPhi2.GetPaintedGraph().GetYaxis().SetRangeUser(0.6,1.0)

plot(cPhi2,"IsoEffVsPhi2")


######## Eff Vs Muon Phi3 ########
cPhi3 = TCanvas("cPhi3", "cPhi3", 700, 700)
cPhi3.SetLeftMargin(0.12)
cPhi3.SetBottomMargin(0.12)
cPhi3.SetRightMargin(0.08);
cPhi3.SetTopMargin(0.08);

f.cd()
all24Phi3 = passedEta3Mu24Phi.Clone()
print "Pass Mu24: ",all24Phi3.GetEntries()
pass24Phi3 = passedEta3IsoMu24Phi.Clone()
print "Pass IsoMu24: ",pass24Phi3.GetEntries()

all24Phi3.Rebin(nPhiBins,"All24Phi3",PhiBins)
pass24Phi3.Rebin(nPhiBins,"Pass24Phi3",PhiBins)

Phi3all24=ROOT.gDirectory.Get("All24Phi3")
dPhi3All24=ROOT.TH1D(Phi3all24)
Phi3pass24=ROOT.gDirectory.Get("Pass24Phi3")
nPhi3Pass24=ROOT.TH1D(Phi3pass24)

effPhi3 = ROOT.TEfficiency(nPhi3Pass24,dPhi3All24)
effPhi3.SetTitle(";Muon #phi;Isolation Efficiency")
setStyle(effPhi3,1)
effPhi3.Draw("")
effPhi3.Paint("")
effPhi3.GetPaintedGraph().GetXaxis().SetTitleOffset(1.4)
effPhi3.GetPaintedGraph().GetYaxis().SetTitleOffset(1.65)
effPhi3.GetPaintedGraph().GetYaxis().SetRangeUser(0.95,1.0)
#effPhi3.GetPaintedGraph().GetYaxis().SetRangeUser(0.6,1.0)

plot(cPhi3,"IsoEffVsPhi3")

