import string
import os

class AirplanesMenu():

    def __init__(self):
        pass

    def header(self):
        print('*'*95,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n {}\n \n {} \n    ".format("*"*95, "{}Airplanes{}".format(" "*25, " "*30), "-"*65))

    def print_airplanes_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header()
            print('Menu\n-----\n1. Create New Airplane\n2. Get All Airplanes\n3. Back to Main menu\n')

            input_command = input('Input Command: ').lower()
            if input_command == '1':
                pass
            elif input_command == '2':
                pass
            elif input_command == '3':
                pass