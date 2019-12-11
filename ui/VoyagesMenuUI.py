from logic.VoyagesLL import VoyagesLL
from modules.Voyages import Voyages
import string
import os

class VoyagesMenu():

    def __init__(self):
        pass

    def header(self, title):
        print('*'*95,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n{}\n \n {} \n    ".format("*"*95, "{}{}{}".format(" "*23, title, " "*30), "-"*65))

    def get_voyage(self):
        pass


    def get_all_voyages(self):
        input_command = ''
        while input_command != 'q':
            self.header('All Voyages')
            print('{:^5}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('ID', 'Insignia', 'Date', 'Destination', 'Captain', 'Copilot', 'Flight Service Manager', 'Flight Attendant'))
            print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('-'*5, '-'*5, '-'*5, '-'*5, '-'*5, '-'*5, '-'*5, '-'*5))
            all_voyages = VoyagesLL().get_voyages()
            counter = 0
            print(all_voyages)
            for line in all_voyages:
                line_counter = counter + 1
                print('{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^10}{}{}'.format(str(line_counter) + '.', all_voyages[counter][0], all_voyages[counter][1], all_voyages[counter][2], all_voyages[counter][3], all_voyages[counter][4], all_voyages[counter][5], all_voyages[counter][6], all_voyages[counter][7]))
                counter += 1
            print('')
            input_command = input('Input Command: ').lower()


               

    def print_voyages_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header('Voyages')
            print('Menu\n-----\n1. Create Voyage\n2. Get All Voyages\n3. Update Voyage\n4. Back to Main menu\n')

            input_command = input('Input Command: ').lower()
            if input_command == '1':
                pass
            elif input_command == '2':
                VoyagesMenu().get_all_voyages()
            elif input_command == '3':
                pass
            elif input_command == '4':
                pass