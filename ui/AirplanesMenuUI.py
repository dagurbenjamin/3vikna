import string
import os
from logic.AirplanesLL import AirplanesLL


class AirplanesMenu():

    def __init__(self):
        pass

    def header(self, title):
        print('*'*95, '\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format(
            '"q" - quitAndSave'))
        print("\n{}\n \n {} \n    ".format(
            "*"*95, "{}{}{}".format(" "*23, title, " "*30), "-"*65))

    def get_all_airplanes(self):
        input_command = ''
        while input_command != 'q':
            self.header('All Airplanes')
            print('{:^20}{:^20}'.format('planeInsignia', 'planeTypeId'))
            print('{:^20}{:^20}'.format('-'*10, '-'*10))
            all_airplanes = AirplanesLL().get_all_airplanes()
            counter = 0
            for line in all_airplanes:
                line_counter = counter + 1
                print('{:^5}{:^5}{:^30}'.format(str(line_counter) + '.',
                                                all_airplanes[counter][0], all_airplanes[counter][1]))
            print('')
            input_command = input("Input command: ").lower()
            if input_command == '1':
                AirplanesMenu().get_airplanetype(all_airplanes[0][1])

    def get_airplanetype(self, planeTypeId):
        one_airplanetype = AirplanesLL().get_info_about_one_airplane(planeTypeId)
        input_command = ''
        while input_command != 'q':
            self.header(planeTypeId)
            print('\n{:^15}{:^32}{:^23}'.format(
                'manufacturer', 'model', 'capacity'))
            print('{:^15}{:^32}{:^25}'.format('-'*15, '-'*8, '-'*10))
            print('{:^15}{:^33}{:^23}\n'.format(one_airplanetype.get_manufacturer(),
                                                one_airplanetype.get_model(), one_airplanetype.get_capacity()))
            print('{:^13}{:^38}{:^14}'.format(
                'emptyWeight', 'maxTakeoffWeight', 'unitThrust'))
            print('{:^15}{:^32}{:^22}'.format(
                '-'*10, '-'*9, '-'*12,))
            print('{:^15}{:^36}{:^15}\n'.format(one_airplanetype.get_eweight(
            ), one_airplanetype.get_fweight(), one_airplanetype.get_thrust()))
            print('{:^13}{:^38}{:^14}'.format(
                'serviceCeiling', 'length', 'height'))
            print('{:^15}{:^32}{:^22}'.format('-'*10, '-'*9, '-'*12))
            print('{:^15}{:^36}{:^15}\n'.format(one_airplanetype.get_ceiling(), one_airplanetype.get_length(
            ), one_airplanetype.get_height()))
            print('{:^35}'.format('wingspan'))
            print('{:^32}'.format('-'*10))
            print('{:^36}\n'.format(one_airplanetype.get_wingspan()))
            print(
                '\n\n1. Back to Main menu\n2. Back to All Airplanes\n3. Back to All Pilots\n')

            input_command = input("Input command: ").lower()
            if input_command == '2':
                EmployeesMenu().get_all_employees()
            elif input_command == '3':
                EmployeesMenu().get_all_pilots('Pilot')

    def print_airplanes_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header('Airplanes')
            print(
                'Menu\n-----\n1. Create New Airplane\n2. Get All Airplanes\n3. Back to Main menu\n')

            input_command = input('Input Command: ').lower()
            if input_command == '1':
                AirplanesMenu().print_create_menu()
            elif input_command == '2':
                AirplanesMenu().get_all_airplanes()
            elif input_command == '3':
                pass

    def print_create_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header('Create New Airplane Or Airplane Type')
            print(
                'Menu\n-----\n1. Create New Airplane\n2. Create New Airplane Type\n')

            input_command = input('Input Command: ').lower()
            if input_command == '1':
                AirplanesMenu().create_airplane()
            elif input_command == '2':
                AirplanesMenu().create_airplane_type()

    def create_airplane(self):
        self.header('Create New Airplane')
        input_command = ''
        new_airplane = ''
        new_airplane_list = []
        while input_command != 'q':
            input_command = input('planeInsignia: ')
            new_airplane_list.append(input_command)
            input_command = input('planeTypeId: ')
            new_airplane_list.append(input_command)
            self.header(new_airplane_list[1])
            print('\n{:^15}{:^23}'.format('planeInsignia', 'planeTypeId'))
            print('{:^15}{:^32}'.format('-'*6, '-'*8,))
            print('{:^15}{:^33}\n'.format(
                new_airplane_list[0], new_airplane_list[1]))
            print('\nIs this correct?\n-----\n1. Yes\n2. No\n')
            input_command = input('Input Command: ')
            if input_command == '1':
                new_airplane = ','.join([str(elem)
                                         for elem in new_airplane_list])
                AirplanesLL().save_new_airplane(new_airplane)
                print('\nAirplane added!\n')
                AirplanesMenu().get_all_airplanes()
            elif input_command == '2':
                continue

    def create_airplane_type(self):
        self.header('Create New Airplane Type')
        input_command = ''
        new_employee = ''
        new_employee_list = []
