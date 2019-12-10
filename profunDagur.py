from logic.EmployeesLL import EmployeesLL
from iolayer.CrewIO import CrewIO
from iolayer.DestinationsIO import DestinationsIO
from iolayer.VoyagesIO import VoyagesIO
from modules.Crew import Crew
from datetime import datetime, date
from modules.Voyages import Voyages
import csv

inputt = "2019-12-20"

def employees_not_working(inputt):
    list_of_non_workers = []
    list_of_workers = []
    x = VoyagesIO().load_voyages_from_file(voyageID="0")
    y = CrewIO().load_crew_from_file(ssn_toFind="0")
    for line in x:
        if line.date == inputt:
            list_of_workers.append(line.captain)
            list_of_workers.append(line.copilot)
            list_of_workers.append(line.FlightServiceManager)
            list_of_workers.append(line.flightAttendant)
    for line in y:
        list_of_non_workers.append(line.social)
    for employee in list_of_non_workers:
        if employee in list_of_workers:
            list_of_non_workers.remove(employee)

    return list_of_non_workers

employees_not_working(inputt)



