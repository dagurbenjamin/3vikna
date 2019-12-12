from logic.EmployeesLL import EmployeesLL
from iolayer.CrewIO import CrewIO
from iolayer.DestinationsIO import DestinationsIO
from iolayer.VoyagesIO import VoyagesIO
from modules.Crew import Crew
from datetime import datetime, date
from modules.Voyages import Voyages
from modules import aircraft
from modules import destinations
from ui.DestinationsMenuUI import DestinationsMenu
from logic.DestinationsLL import DestinationsLL
import csv


def get_all_destinations():
    x = DestinationsIO().load_destination_from_file(destination_id="0")
    for line in x:
        destination = line.destination
    input_command = ''
    while input_command != 'q':
        header = 'All Destinations'
        print(header)
        print(destination)
        if input_command == '1':
            DestinationsMenu().get_destination('GOH')


get_all_destinations()