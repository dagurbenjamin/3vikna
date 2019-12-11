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


def create_new_employee(self):
    self.header('Add New Airplane')
    input_command = ''
    new_plane = ''
    new_destination_list = []
    while input_command != 'q':
        input_command = input('Create ID for New Destination: ')
        new_destination_list.append(input_command)
        input_command = input('Name of Destination: ')
        new_destination_list.append(input_command)
        input_command = input('Name of Country: ')
        new_destination_list.append(input_command)
        input_command = input('Distance from KEF: ')
        new_destination_list.append(input_command)
        input_command = input('Name of Emergency Contact: ')
        new_destination_list.append(input_command)
        input_command = input('Phone number of Emergency Contact: ')
        new_destination_list.append(input_command)
        input_command = input('Flight time to Destination: ')
        new_destination_list.append(input_command)
        input_command = input('Insert Destination Number: ')
        new_destination_list.append(input_command)
        self.header(new_destination_list[1])
        print('\n{:^15}{:^32}{:^23}'.format('Role', 'Destination', 'Emergency Contact', 'Emergency Number'))
        print('{:^15}{:^32}{:^25}'.format('-' * 6, '-' * 8, '-' * 12, '-' * 12))
        print('{:^15}{:^33}{:^23}\n'.format(new_destination_list[1], new_destination_list[2], new_destination_list[4],
                                            new_destination_list[5]))
        print('{:^13}{:^38}{:^14}{:^16}'.format('ID', 'Distance', 'Flight Time', 'Destination Number'))
        print('{:^15}{:^32}{:^22}{}'.format('-' * 10, '-' * 9, '-' * 12, '-' * 12))
        print('{:^15}{:^36}{:^15}{}\n'.format(new_destination_list[0], new_destination_list[3], new_destination_list[6],
                                              new_destination_list[7]))
        print('\nIs this correct?\n-----\n1. Yes\n2. No\n')
        input_command = input('Input Command: ')
        if input_command == '1':
            new_destination = ','.join([str(elem) for elem in new_destination_list])
            DestinationsLL().save_new_destination(new_destination)
            print('\nDestination added!\n')
            DestinationsMenu().get_all_destinations()
        elif input_command == '2':
            continue
