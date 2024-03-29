from logic.DestinationsLL import DestinationsLL
from modules.destinations import Destinations
import string
import os


class DestinationsMenu():

    def __init__(self):
        pass

    def header(self, title):
        '''
        This function puts a header on each page
        '''
        os.system('cls')
        print('*'*75, '\n')
        print('{}NaN Air   ''\033[91m                 {} \033[00m'.format(' '*31,
                                                                          '"q" - quitAndSave\n'))
        print('*'*75, '\n')
        print('{:^70}\n'.format(title))

    def get_destination(self, destination_id):
        '''
        This function gets the destionation based on user input, the destionation ID
        and prints it out
        '''
        one_destination = DestinationsLL().get_destination(destination_id)
        input_command = ''
        while input_command != 'q':
            self.header(str(one_destination.get_country() +
                            '-' + one_destination.get_destination()))
            print('\n{:^14}{:^30}{:^25}'.format(
                'Airport', 'Country', 'Distance'))
            print('{:^15}{:^27}{:^27}'.format('-'*6, '-'*10, '-'*12))
            print('{:^7}{:^33}{:^25}\n'.format(one_destination.get_destination(
            )+" Airport", one_destination.get_country(), one_destination.get_distance()+" km"))
            print('{:^14}{:^34}{:^18}'.format('Contact name ',
                                              'Emergency number', 'Flight time'))
            print('{:^15}{:^26}{:^30}'.format('-'*10, '-'*9, '-'*12))
            print('{:^15}{:^26}{:^30}\n'.format(one_destination.get_contactname(), one_destination.get_emergencynumber(
            ), one_destination.get_flighttime()))
            print('{:^14}'.format('Destination Number'))
            print('{:^15}'.format('-' * 10))
            print('{:^15}\n'.format(one_destination.get_destinationnumber()))
            print('\n\n1. Back to Main menu\n2. Back to All Destinations\n')
            input_command = input('Input command: ').lower()
            if input_command == '1':
                pass
            elif input_command == '2':
                DestinationsMenu().get_all_destinations()

    def get_all_destinations(self):
        '''
        This function gets all the destionations and prints them out with ID, city and country
        '''
        input_command = ''
        while input_command != 'q':
            self.header('All Destinations')
            print('{:^22}{:>10}/{}'.format('ID', 'City', 'Country'))
            print('{:^22}{:^22}'.format('-'*5, '-'*20))
            all_destinations = DestinationsLL().get_all_destinations()
            counter = 0
            for line in all_destinations:
                line_counter = counter + 1
                print('{:^5}{:^12}{:^35}'.format(str(line_counter) + '.',
                                                 all_destinations[counter][0], all_destinations[counter][1] + '/' + all_destinations[counter][2]))
                counter += 1
            print('\n"b".....Back to Destination Menu')
            input_command = input("Input command: ").lower()
            for item in range(1, len(all_destinations) + 1):
                if input_command == str(item):
                    DestinationsMenu().get_destination(
                        all_destinations[item - 1][0])
                elif input_command == 'b':
                    DestinationsMenu().print_destinations_menu()

    def create_new_destination(self):
        '''
        This function takes in the information for a new destination
        and sends the info to be stored
        '''
        self.header('Add New Destination')
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
            for the_input in input_command:
                if input_command.isdigit():
                    new_destination_list.append(input_command)
                    break
                else:
                    print('Enter valid distance.')
                    input_command = input('Distance from Kef: ')
            input_command = input('Name of Emergency Contact: ')
            new_destination_list.append(input_command)
            input_command = input('Phone number of Emergency Contact: ')
            for the_input in input_command:
                if input_command.isdigit() and len(input_command) <= 15:
                    new_destination_list.append(input_command)
                    break
                else:
                    print('Enter a valid phone number.')
                    input_command = input(
                        'Phone number of Emergency Contact: ')
            input_command = input('Flight time to Destination: ')
            new_destination_list.append(input_command)
            input_command = input('Insert Destination Number: ')
            for the_input in input_command:
                if input_command.isdigit() and len(input_command) == 2:
                    new_destination_list.append(input_command)
                    break
                else:
                    print('Enter a valid Destination Number.')
                    input_command = input('Insert Destination Number: ')
            self.header(new_destination_list[1])
            print('\n{:^15}{:^32}{:^23}'.format('Destination',
                                                'Country', 'Emergency Contact', 'Emergency Number'))
            print('{:^15}{:^32}{:^25}'.format(
                '-' * 6, '-' * 8, '-' * 12, '-' * 12))
            print(
                '{:^15}{:^33}{:^23}\n'.format(new_destination_list[1], new_destination_list[2], new_destination_list[4],
                                              new_destination_list[5]))
            print('{:^13}{:^38}{:^14}'.format('ID', 'Distance', 'Flight Time'))
            print('{:^15}{:^32}{:^22}'.format(
                '-' * 10, '-' * 9, '-' * 12, '-' * 12))
            print('{:^15}{:^36}{:^15}\n'.format(new_destination_list[0], new_destination_list[3],
                                                new_destination_list[6], new_destination_list[7]))
            print('{:^13}'.format('Destination Number'))
            print('{:^15}'.format('-' * 10))
            print('{:^15}\n'.format(new_destination_list[7]))
            print('\nIs this correct?\n-----\n1. Yes\n2. No\n')
            input_command = input('Input Command: ')
            if input_command == '1':
                new_destination = ','.join(
                    [str(elem) for elem in new_destination_list])
                DestinationsLL().save_new_destination(new_destination)
                print('\nDestination added!\n')
                DestinationsMenu().get_all_destinations()
            elif input_command == '2':
                continue

    def update_this_destination(self, destination_id):
        '''
        This function takes inputs from user that is sent to other 
        functions that store the new information
        '''
        one_destination = DestinationsLL().get_destination(destination_id)
        print(one_destination)
        input_command = ''
        while input_command != 'q':
            self.header(str(one_destination.get_country() +
                            '-' + one_destination.get_destination()))
            print('\n{:^14}{:^30}{:^25}'.format(
                'Airport', 'Country', 'Distance'))
            print('{:^15}{:^27}{:^27}'.format('-'*6, '-'*10, '-'*12))
            print('{:^7}{:^33}{:^25}\n'.format(one_destination.get_destination(
            )+" Airport", one_destination.get_country(), one_destination.get_distance()+" km"))
            print('{:^14}{:^34}{:^18}'.format('Contact name ',
                                              'Emergency number', 'Flight time'))
            print('{:^15}{:^26}{:^30}'.format('-'*10, '-'*9, '-'*12))
            print('{:^15}{:^26}{:^30}\n'.format(one_destination.get_contactname(), one_destination.get_emergencynumber(
            ), one_destination.get_flighttime()))
            print('{:^14}'.format('Destination Number'))
            print('{:^15}'.format('-' * 10))
            print('{:^15}\n'.format(one_destination.get_destinationnumber()))
            print('\nWhat would you like to update?\n------\n1. Contact name\n2. Emergency number\nb. Back one page\n')

            input_command = input('Input command: ').lower()
            if input_command == '1':
                input_command = input('\nNew contact name: ')
                one_destination.set_contactname(input_command)
                one_destination_list = str(one_destination).split(',')
                DestinationsLL().change_the_big_destinations_list(
                    one_destination.get_id(), one_destination_list)
                continue
            elif input_command == '2':
                input_command = input('\nNew emergency number: ')
                for the_input in input_command:
                    if input_command.isdigit() and len(input_command) <= 15:
                        one_destination.set_emergencynumber(input_command)
                        break
                    else:
                        print('Enter a valid phone number.')
                        input_command = input('New emergency number: ')
                one_destination_list = str(one_destination).split(',')
                DestinationsLL().change_the_big_destinations_list(
                    one_destination.get_id(), one_destination_list)
                continue
            elif input_command == 'b':
                DestinationsMenu().update_destination()

    def update_destination(self):
        '''
        This function shows what destinations can be updated so user
        can choose which one he wants to update
        '''
        input_command = ''
        while input_command != 'q':
            self.header('All Destinations that can be updated')
            print('{:^22}{:>10}/{}'.format('ID', 'City', 'Country'))
            print('{:^22}{:^22}'.format('-' * 5, '-' * 20))
            all_destinations = DestinationsLL().get_all_destinations()
            counter = 0
            for line in all_destinations:
                line_counter = counter + 1
                print('{:^5}{:^12}{:^35}'.format(str(line_counter) + '.', all_destinations[counter][0],
                                                 all_destinations[counter][1] + '/' + all_destinations[counter][2]))
                counter += 1
            print('\n"b".....Back to Destination Menu')
            input_command = input("Input command: ").lower()
            for item in range(1, len(all_destinations) + 1):
                if input_command == str(item):
                    DestinationsMenu().update_this_destination(
                        all_destinations[item - 1][0])
                elif input_command == 'b':
                    DestinationsMenu().print_destinations_menu()

    def print_destinations_menu(self):
        '''
        This function prints out the destination menu 
        so user can choose what he wants to do
        '''
        input_command = ''
        while input_command != 'q':
            self.header('Destinations')
            print('Menu\n----\n1. Create New Destination\n2. Get all destinations\n3. Update destination\n4. Back to Main menu\n')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                DestinationsMenu().create_new_destination()
            elif input_command == '2':
                DestinationsMenu().get_all_destinations()
            elif input_command == '3':
                DestinationsMenu().update_destination()
            elif input_command == '4':
                pass
