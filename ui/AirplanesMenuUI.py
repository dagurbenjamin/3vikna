import string
import os
from logic.AirplanesLL import AirplanesLL
from logic.EmployeesLL import EmployeesLL


class AirplanesMenu():

    def __init__(self):
        pass

    def header(self, title):
        '''
        This function clears the screen and adds a header on the screen 
        '''
        os.system('cls')
        print('*'*75, '\n')
        print('{}NaN Air   ''\033[91m                 {} \033[00m'.format(' '*31,
                                                                          '"q" - quitAndSave\n'))
        print('*'*75, '\n')
        print('{:^70}\n'.format(title))

    def get_all_airplanes(self):
        '''
        This function prints out all the airplanes
        '''
        input_command = ''
        while input_command != 'q':
            self.header('All Airplanes')
            print('{:^20}{:^10}'.format('Insignia', 'Type'))
            print('{:^20}{:^10}'.format('-'*10, '-'*10))
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
                'Menu\n-----\nBack To Airplanes Menu....."b"\n')
            input_command = input("Input command: ").lower()
            for item in range(1, len(all_airplanes) + 1):
                if input_command == str(item):
                    AirplanesMenu().get_airplanetype(
                        all_airplanes[item - 1][1], all_airplanes[item - 1][0])
                elif input_command == 'b':
                    AirplanesMenu().print_airplanes_menu()

    def get_airplanetype(self, planeTypeId, planeInsignia):
        '''
        This function prints out a page with the information
        containing the information of the type of airplane inputted
        '''
        one_airplanetype = AirplanesLL().get_info_about_one_airplane(planeTypeId)
        input_command = ''
        while input_command != 'q':
            self.header(planeTypeId)
            print('\n{:^19}{:^32}{:^23}'.format(
                'Manufacturer', 'Model', 'Capacity'))
            print('{:^19}{:^32}{:^25}'.format('-'*15, '-'*8, '-'*10))
            print('{:^19}{:^33}{:^21}\n'.format(one_airplanetype.get_manufacturer(),
                                                one_airplanetype.get_model(), one_airplanetype.get_capacity()))
            print('{:^18}{:^37}{:^13}'.format(
                'Empty Weight', 'Max Take off Weight', 'Unit Thrust'))
            print('{:^19}{:^34}{:^18}'.format(
                '-'*10, '-'*9, '-'*12,))
            print('{:^19}{:^34}{:^16}\n'.format(one_airplanetype.get_eweight(
            ), one_airplanetype.get_fweight(), one_airplanetype.get_thrust()))
            print('{:^17}{:^36}{:^17}'.format(
                'Service Ceiling', 'Length', 'Height'))
            print('{:^19}{:^33}{:^19}'.format('-'*10, '-'*9, '-'*8))
            print('{:^19}{:^33}{:^18}\n'.format(one_airplanetype.get_ceiling(), one_airplanetype.get_length(
            ), one_airplanetype.get_height()))
            print('{:^19}'.format('Wingspan'))
            print('{:^19}'.format('-'*10))
            print('{:^18}\n'.format(one_airplanetype.get_wingspan()))
            print('Menu\n-----\n1. Employees that are licenced for this airplane\n2. Back to All Airplanes\n3. Back to Main menu\n')
            input_command = input("Input command: ").lower()
            if input_command == '1':
                AirplanesMenu().employees_licenced_for_certain_airplane(planeTypeId, planeInsignia)
            elif input_command == '2':
                AirplanesMenu().get_all_airplanes()

    def print_airplanes_menu(self):
        '''
        This function prints out the airplane menu
        '''
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
        '''
        This function prints out the create airplane menu
        '''
        input_command = ''
        while input_command != 'q':
            self.header('Create New Airplane Or Airplane Type')
            print(
                'Menu\n-----\n1. Create New Airplane\n2. Create New Airplane Type\n\n3. Back to Airplanes menu\n')
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
        '''
        This function takes the user input and creates
        a new airplane and sends the information to be written
        '''
        self.header('Create New Airplane')
        input_command = ''
        new_airplane = ''
        new_airplane_list = []
        while input_command != 'q':
            input_command = input('Plane Insignia: TF-')
            new_airplane_list.append("TF-" + input_command)
            input_command = input('Plane Type: NA')
            new_airplane_list.append('NA' + input_command)
            self.header(new_airplane_list[1])
            print('\n{:^30}{:^30}'.format('Plane Insignia', 'Plane Type'))
            print('{:^30}{:^30}'.format('-'*6, '-'*8,))
            print('{:^30}{:^30}\n'.format(
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
        '''
        This function creates a new type of airplane type
        '''
        self.header('Create New Airplane Type')
        input_command = ''
        new_airplane_type = ''
        new_airplane_type_list = []
        while input_command != 'q':
            input_command = input('Plane Type: NA')
            new_airplane_type_list.append('NA' + input_command)
            input_command = input('Manufacturer: ')
            new_airplane_type_list.append(input_command)
            input_command = input('Model: ')
            new_airplane_type_list.append(input_command)
            input_command = input('Capacity: ')
            for the_input in input_command:
                if input_command.isdigit():
                    new_airplane_type_list.append(input_command)
                    break
                else:
                    print('Enter valid Capacity.')
                    input_command = input('Capacity: ')
            input_command = input('Empty Weight: ')
            for the_input in input_command:
                if input_command.isdigit():
                    new_airplane_type_list.append(input_command)
                    break
                else:
                    print('Enter valid Empty Weight.')
                    input_command = input('Empty Weight: ')
            input_command = input('Max Take off Weight: ')
            for the_input in input_command:
                if input_command.isdigit():
                    new_airplane_type_list.append(input_command)
                    break
                else:
                    print('Enter valid Max Take off Weight.')
                    input_command = input('Max Take off Weight: ')
            input_command = input('Unit Thrust: ')
            for the_input in input_command:
                if input_command.isdigit():
                    new_airplane_type_list.append(input_command)
                    break
                else:
                    print('Enter valid Unit Thrust.')
                    input_command = input('Unit Thrust: ')
            input_command = input('Service Ceiling: ')
            for the_input in input_command:
                if input_command.isdigit():
                    new_airplane_type_list.append(input_command)
                    break
                else:
                    print('Enter valid Service Ceiling.')
                    input_command = input('Service Ceiling: ')
            input_command = input('Length: ')
            for the_input in input_command:
                if input_command.isdigit():
                    new_airplane_type_list.append(input_command)
                    break
                else:
                    print('Enter valid Length.')
                    input_command = input('Length: ')
            input_command = input('Height: ')
            for the_input in input_command:
                if input_command.isdigit():
                    new_airplane_type_list.append(input_command)
                    break
                else:
                    print('Enter valid Height.')
                    input_command = input('Height: ')
            input_command = input('Wingspan: ')
            for the_input in input_command:
                if input_command.isdigit():
                    new_airplane_type_list.append(input_command)
                    break
                else:
                    print('Enter valid Wingspan.')
                    input_command = input('Wingspan: ')
            self.header('New Airplane Type')
            print('\n{:^15}{:^32}{:^23}'.format(
                'Plane type', 'Manufacturer', 'Model'))
            print('{:^15}{:^32}{:^25}'.format('-'*15, '-'*8, '-'*10))
            print('{:^15}{:^33}{:^23}\n'.format(
                new_airplane_type_list[0], new_airplane_type_list[1], new_airplane_type_list[2]))
            print('\n{:^15}{:^32}{:^23}'.format(
                'Capacity', 'Empty Weight', 'Max Take off Weight'))
            print('{:^15}{:^32}{:^25}'.format('-'*15, '-'*8, '-'*15))
            print('{:^15}{:^33}{:^23}\n'.format(
                new_airplane_type_list[3], new_airplane_type_list[4], new_airplane_type_list[5]))
            print('\n{:^15}{:^32}{:^23}'.format(
                'Unit Thrust', 'Service Ceiling', 'Length'))
            print('{:^15}{:^32}{:^25}'.format('-'*15, '-'*8, '-'*15))
            print('{:^15}{:^33}{:^23}\n'.format(
                new_airplane_type_list[6], new_airplane_type_list[7], new_airplane_type_list[8]))
            print('\n{:^15}{:^23}'.format('Height', 'Wingspan'))
            print('{:^15}{:^25}'.format('-'*15, '-'*15))
            print('{:^15}{:^23}\n'.format(
                new_airplane_type_list[9], new_airplane_type_list[10]))
            print(
                '\n\nMenu\n-----\nDo you want to add this airplane type?\n-----\n1. Yes\n2. No\n')
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
        '''
        This function prints out all employees licensed for the inputted plane type
        '''
        input_command = ''
        while input_command != 'q':
            self.header(f'Employees licenced for {planeTypeId}')
            print('{:^62}'.format('-'*20))
            all_employees = EmployeesLL().get_all_employees_with_all_informations()
            for employee in all_employees:
                if employee[4] == planeTypeId:
                    print('{:^63}'.format(f'{employee[1]}'))
            print(
                'Menu\n-----\n1. Back To Airplane\n2. Back To Airplanes Menu\n')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                AirplanesMenu().get_airplanetype(planeTypeId, planeInsignia)
            if input_command == '2':
                AirplanesMenu().print_airplanes_menu()
