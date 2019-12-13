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


def header(title):
    print('*' * 95, '\n')
    print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
    print("\n{}\n \n {} \n    ".format("*" * 95, "{}{}{}".format(" " * 23, title, " " * 30), "-" * 65))

"""def getinations():
    input_command = ''
    #while input_command != 'q':
        #self.header('All Destinations')
    x = DestinationsIO().load_destination_from_file(destination_id="0")
    print('All Destinations \n----')
    counter = 0
    for line in x:
        counter += 1 
        destination = line.destination
        print(f"{str(destination)}")"""

def get_all_destination(self):
    input_command = ''
    while input_command != 'q':
        self.header('All Destinations')
        print('{:^15}{:^20}{:^21}'.format('D-ID', 'Destination', 'Country'))
        print('{:^15}{:^19}{:^22}'.format('-'*10, '-'*17, '-'*10))
        all_destinations = DestinationsLL().get_all_destinations()
        counter = 0
        for line in all_destinations:
            line_counter = counter + 1
            print('{:^5}{:^5}{:^30}{:^10}'.format(str(line_counter) + '.' ,all_destinations[counter][0], all_destinations[counter][1], all_destinations[counter][2]))
            counter += 1
        print('')
        print('"b".......Back one page\n')
        input_command = input("Input command: ").lower()
        for item in range(1,len(all_destinations) + 1):
            if input_command == str(item):
                DestinationsMenu().get_destination(all_destinations[item - 1][0])
            elif input_command == 'p':
                pass


get_all_destination(self)