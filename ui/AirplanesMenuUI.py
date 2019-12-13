import string
import os
from logic.AirplanesLL import AirplanesLL
from logic.EmployeesLL import EmployeesLL


class AirplanesMenu():

    def __init__(self):
        pass

    def header(self, title):
        os.system('cls')
        print('*'*75, '\n')
        print('{}NaN Air   ''\033[91m                 {} \033[00m'.format(' '*31,
            '"q" - quitAndSave\n'))
        print('*'*75, '\n')
        print('{:^70}\n'.format(title))

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
                counter += 1
            print('')
            #print('Airplane status......."as"')
            print(
                'Menu\n-----\nBack To Airplanes Menu....."am"\nBack To Main Menu........."mm" \n')
            input_command = input("Input command: ").lower()
            for item in range(1, len(all_airplanes) + 1):
                if input_command == str(item):
                    AirplanesMenu().get_airplanetype(
                        all_airplanes[item - 1][1], all_airplanes[item - 1][0])
                elif input_command == 'am':
                    AirplanesMenu().print_airplanes_menu()
                elif input_command == 'mm':
                    pass

    def get_airplanetype(self, planeTypeId, planeInsignia):
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
                '\n\n1. Employees that are licenced for this airplane\n2. Back to All Airplanes\n3. Back to Main menu')
            print('')
            input_command = input("Input command: ").lower()
            if input_command == '1':
                AirplanesMenu().employees_licenced_for_certain_airplane(planeTypeId, planeInsignia)
            elif input_command == '2':
                AirplanesMenu().get_all_airplanes()

    def print_airplanes_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header('Airplanes')
            print(
                'Menu\n-----\n1. Create New Airplane\n2. Get All Airplanes\n3. Back to Main menu\n')
            print('')
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
                'Menu\n-----\n1. Create New Airplane\n2. Create New Airplane Type\n\n3. back to Airplanes menu')
            print('')
            print('')
            print('')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                AirplanesMenu().create_airplane()
            elif input_command == '2':
                AirplanesMenu().create_airplane_type()
            elif input_command == '3':
                AirplanesMenu().print_airplanes_menu()

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
            print('\nDo you want to add this airplane?\n-----\n1. Yes\n2. No\n')
            print('')
            print('')
            input_command = input('Input Command: ')
            if input_command == '1':
                new_airplane = ','.join([str(elem)
                                         for elem in new_airplane_list])
                AirplanesLL().save_new_airplane(new_airplane)
                AirplanesMenu().print_create_menu()
            elif input_command == '2':
                continue

    def create_airplane_type(self):
        self.header('Create New Airplane Type')
        input_command = ''
        new_airplane_type = ''
        new_airplane_type_list = []
        while input_command != 'q':
            input_command = input('planeTypeId: ')
            new_airplane_type_list.append(input_command)
            input_command = input('manufacturer: ')
            new_airplane_type_list.append(input_command)
            input_command = input('model: ')
            new_airplane_type_list.append(input_command)
            input_command = input('capacity: ')
            new_airplane_type_list.append(input_command)
            input_command = input('emptyWeight: ')
            new_airplane_type_list.append(input_command)
            input_command = input('maxTakeoffWeight: ')
            new_airplane_type_list.append(input_command)
            input_command = input('unitThrust: ')
            new_airplane_type_list.append(input_command)
            input_command = input('serviceCeiling: ')
            new_airplane_type_list.append(input_command)
            input_command = input('length: ')
            new_airplane_type_list.append(input_command)
            input_command = input('height: ')
            new_airplane_type_list.append(input_command)
            input_command = input('wingspan: ')
            new_airplane_type_list.append(input_command)
            self.header('New Airplane Type')
            print('\n{:^15}{:^32}{:^23}'.format(
                'planeTypeId', 'manufacturer', 'model'))
            print('{:^15}{:^32}{:^25}'.format('-'*15, '-'*8, '-'*10))
            print('{:^15}{:^33}{:^23}\n'.format(
                new_airplane_type_list[0], new_airplane_type_list[1], new_airplane_type_list[2]))
            print('\n{:^15}{:^32}{:^23}'.format(
                'capacity', 'emptyWeight', 'maxTakeoffWeight'))
            print('{:^15}{:^32}{:^25}'.format('-'*15, '-'*8, '-'*15))
            print('{:^15}{:^33}{:^23}\n'.format(
                new_airplane_type_list[3], new_airplane_type_list[4], new_airplane_type_list[5]))
            print('\n{:^15}{:^32}{:^23}'.format(
                'unitThrust', 'serviceCeiling', 'length'))
            print('{:^15}{:^32}{:^25}'.format('-'*15, '-'*8, '-'*15))
            print('{:^15}{:^33}{:^23}\n'.format(
                new_airplane_type_list[6], new_airplane_type_list[7], new_airplane_type_list[8]))
            print('\n{:^15}{:^23}'.format('height', 'wingspan'))
            print('{:^15}{:^25}'.format('-'*15, '-'*15))
            print('{:^15}{:^23}\n'.format(
                new_airplane_type_list[9], new_airplane_type_list[10]))
            print('\nDo you want to add this airplane type?\n-----\n1. Yes\n2. No\n')
            input_command = input('Input Command: ')
            print('')
            print('')
            if input_command == '1':
                new_airplane_type = ','.join([str(elem)
                                              for elem in new_airplane_type_list])
                AirplanesLL().save_new_airplane_info(new_airplane_type)
                AirplanesMenu().print_create_menu()
            elif input_command == '2':
                continue

    def employees_licenced_for_certain_airplane(self, planeTypeId, planeInsignia):
        input_command = ''
        while input_command != 'q':
            self.header(f'Employees licenced for {planeTypeId}')
            print('{:^60}'.format('-'*40))
            all_employees = EmployeesLL().get_all_employees_with_all_informations()
            for employee in all_employees:
                if employee[4] == planeTypeId:
                    print('{:^63}'.format(f'{employee[1]}'))
            print(
                'Menu\n-----\n1. Back To Airplane\n2. Back To Airplanes Menu')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                AirplanesMenu().get_airplanetype(planeTypeId, planeInsignia)
            if input_command == '2':
                AirplanesMenu().print_airplanes_menu()
