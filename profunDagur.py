
from iolayer.CrewIO import CrewIO
from iolayer.DestinationsIO import DestinationsIO
from iolayer.VoyagesIO import VoyagesIO
from modules.Crew import Crew
from datetime import datetime, date
from modules.Voyages import Voyages
import csv
voyageID = "0"
inputt = "2019-12-20"

def employees_working(self, inputt):
    x = VoyagesIO().load_voyages_from_file(voyageID)
    for line in x:
        if line.date == inputt:
            return line.captain,line.copilot,line.flightAttendant,line.FlightServiceManager,line.destination
        else:
            False

employees_working(self, inputt)


