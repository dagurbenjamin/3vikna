import string
import os

class VoyagesMenu():

    def __init__(self):
        pass

    def header(self):
        print('*'*65,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n {}\n \n {} \n    ".format("*"*65, "{}Voyages{}".format(" "*25, " "*30), "-"*65))

    def print_voyages_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header()
            print('Menu\n-----\n1. Create Voyage\n2. Get All Voyages\n3. Update Voyage\n4. Back to Main menu\n')

            input_command = input('Input Command: ').lower()
            if input_command == '1':
                pass
            elif input_command == '2':
                pass
            elif input_command == '3':
                pass
            elif input_command == '4':
                pass