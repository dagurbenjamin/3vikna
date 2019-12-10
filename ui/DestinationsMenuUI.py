from logic.DestinationsLL import DestinationsLL
from modules.destinations import Destinations
import string
import os

class DestinationsMenu():

    def __init__(self):
        pass

    def header(self, title):
        print('*'*75,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n {}\n \n {} \n    ".format("*"*75, "{}{}{}".format(" "*25, title, " "*30), "-"*65))



    


    def get_destination(self, destination_id):
        one_destination = DestinationsLL().get_destination(destination_id)
        print(one_destination)
        input_command = ''
        while input_command != 'q':
            self.header(str(one_destination.get_country() + '-' + one_destination.get_destination()))
            print('\n{:^15}{:^32}{:^23}'.format('Airport','Country','Distance'))
            print('{:^15}{:^32}{:^25}'.format('-'*6,'-'*8,'-'*12))
            print('{:^7}{:^37}{:^21}\n'.format(one_destination.get_destination()+" Airport" ,one_destination.get_country() ,one_destination.get_distance()+" km"))
            print('{:^16}{:^34}{:^12}{:^29}'.format('Contact name ','Emergency number','Flight time', 'Destination Number'))
            print('{:^15}{:^32}{:^22}{}'.format('-'*10,'-'*9,'-'*12,'-'*12))
            print('{:^15}{:^34}{:^15}{:^25}\n'.format(one_destination.get_contactname(), one_destination.get_emergencynumber(), one_destination.get_flighttime(), one_destination.get_destinationnumber()))
            print('\n\n1. Back to Main menu\n2. Back to All Destinations\n')

            input_command = input('Input command: ').lower()
            if input_command == '1':
                pass
            elif input_command == '2':
                DestinationsMenu().get_all_destinations()

    def get_all_destinations(self):
        input_command = ''
        while input_command != 'q':
            self.header('All Destinations')
            print('Menu\n-----\n1. Nuuk/Greenland\n2. Kulusuk/Greenland\n3. Torshavn/Faroe islands\n4. Tingwall/Shetland\n5. Longyearbyen/Svalbard\n')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                DestinationsMenu().get_destination('GOH')
            elif input_command == '2':
                pass
            elif input_command == '3':
                pass
            elif input_command == '4':
                pass
            elif input_command == '5':
                pass

    def print_destinations_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header('Destinations')
            print('Menu\n-----\n1. Create Destination\n2. Get all destinations\n3. Update destination\n4. Back to Main menu\n')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                pass
            elif input_command == '2':
                DestinationsMenu().get_all_destinations()
            elif input_command == '3':
                pass
            elif input_command == '4':
                pass
            elif input_command == '5':
                pass
