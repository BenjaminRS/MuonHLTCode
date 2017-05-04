// -*- C++ -*-
// Package:    Skim/SelectEvents
// Class:      SelectEvents
/**\class SelectEvents SelectEvents.cc Skim/SelectEvents/plugins/SelectEvents.cc
 Description: A file skimmer based on event list
 Implementation:
     Distilled from Nov 2014 version
*/
// Original Author:  Benjamin Radburn-Smith
//         Created:  Sat, 22 Apr 2017 12:00:51 GMT

#include <memory>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include <iostream>
#include <fstream>
#include <string>

class SelectEvents : public edm::stream::EDFilter<> {
   public:
      explicit SelectEvents(const edm::ParameterSet&);
      ~SelectEvents();
      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   private:
      virtual void beginStream(edm::StreamID) override;
      virtual bool filter(edm::Event&, const edm::EventSetup&) override;
      virtual void endStream() override;
	std::string filename_;
};

SelectEvents::SelectEvents(const edm::ParameterSet& iConfig){
	filename_ = iConfig.getParameter<std::string>("Filename");
}

SelectEvents::~SelectEvents(){}

bool SelectEvents::filter(edm::Event& iEvent, const edm::EventSetup& iSetup){
	using namespace edm;
	std::ifstream fin(filename_.c_str());
	if (fin.fail()) std::cout << "Error could not open file\n";
	std::string str;
	double RunNumber(0);
	double LumiNumber(0);
	double EventNumber(0);
	while (!fin.eof()){
		std::getline(fin,str,'\n');
		if (!str.empty()){
			char *tempstr = (char*)str.c_str();
			char delims[] = ":";
			char *result = std::strtok( tempstr, delims );
			std::string temp=result;
			RunNumber = atof(temp.c_str());
			result = strtok( NULL, delims );
			temp=result;
			LumiNumber = atof(temp.c_str());
			result = strtok( NULL, delims );
			temp=result;
			EventNumber = atof(temp.c_str());
			if (iEvent.id().run() == RunNumber && iEvent.id().luminosityBlock() == LumiNumber && iEvent.id().event() == EventNumber){
				std::cout << "Found: "<< iEvent.id() << std::endl;
				return true;
			}
		}//str not empty 
	}//file loop
	return false;
}

void SelectEvents::beginStream(edm::StreamID){}

void SelectEvents::endStream() {}

void SelectEvents::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(SelectEvents);
