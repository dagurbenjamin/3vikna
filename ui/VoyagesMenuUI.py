from logic.VoyagesLL import VoyagesLL
from modules.Voyages import Voyages
from logic.FlightsLL import FlightsLL
from logic.DestinationsLL import DestinationsLL
from logic.EmployeesLL import EmployeesLL
from modules.destinations import Destinations
from logic.AirplanesLL import AirplanesLL
import string
import os

class VoyagesMenu():

    def __init__(self):
        pass

    def header(self, title):
        print('*'*95,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n{}\n \n {} \n    ".format("*"*95, "{}{}{}".format(" "*23, title, " "*30), "-"*65))

    def create_voyage(self):
        input_command = ''
        new_voyage = ''
        new_voyage_list = []
        while input_command != 'q':
            self.header('Create New Voyage')
            input_command = input('Airplane: ').upper()
            new_voyage_list.append(input_command)
            print(' {}\n {}\n'.format('Flight 1', '-'*11))
            input_command = input('Destination: ').upper()
            new_voyage_list.append(input_command)
            print('Departure location: {}'.format('KEF'))
            input_command = 'KEF'
            new_voyage_list.append(input_command)
            input_command = input('Departure time: ')
            new_voyage_list.append(input_command)
            input_command = input('Date: ')
            new_voyage_list.append(input_command)

            print('\n {}\n {}\n'.format('Flight 2', '-'*11))
            input_command = new_voyage_list[2]
            new_voyage_list.append(input_command)
            print('Destination: {}'.format(input_command))

            input_command = new_voyage_list[1]
            new_voyage_list.append(input_command)
            print('Departure location: {}'.format(input_command))

            input_command = new_voyage_list[3]
            destination = DestinationsLL().get_destination(new_voyage_list[1])
            flight_time = destination.get_flighttime()
            departure_time = new_voyage_list[3]
            departure_hour = int(departure_time[0:2])
            flight_time_hour = int(flight_time[1:3])
            flight_2_departure_hour = str(departure_hour + flight_time_hour + 1)
            flight_2_departure_time = flight_2_departure_hour + new_voyage_list[3][2:]
            
            new_voyage_list.append(flight_2_departure_time)
            print('Departure time: {}'.format(flight_2_departure_time))

            input_command = new_voyage_list[4]
            new_voyage_list.append(input_command)
            print('Date: {}\n'.format(input_command))            
            airplane_check = AirplanesLL().is_airplane_available(new_voyage_list[4], new_voyage_list[0])
            if airplane_check:
                print('Menu\n{}'.format('-'*5))
                print('1. Save Voyage')
                print('2. Cancel')
                input_command = input('Input Command: ')
                if input_command == '1':
                    VoyagesLL().create_voyage(new_voyage_list)
                elif input_command == '2':
                    VoyagesMenu().print_voyages_menu()
            else:
                while airplane_check == False:
                    print('Airplane is unavailable!\n{}'.format('-'*21))
                    input_command = input('Enter available airplane: ').upper()
                    print('')
                    new_voyage_list[0] = input_command
                    airplane_check = AirplanesLL().is_airplane_available(new_voyage_list[4], new_voyage_list[0])
                print('Menu\n{}'.format('-'*5))
                print('1. Save Voyage')
                print('2. Cancel\n')
                input_command = input('Input Command: ')
                if input_command == '1':
                    
                elif input_command == '2':
                    VoyagesMenu().print_voyages_menu()
                

                
                
                



                
    
                
        
            
                

            
            
            





    def get_voyage(self, voyage_id):
        flights = FlightsLL().get_voyage_flights(voyage_id)
        first_destination = DestinationsLL().get_destination(flights[0].get_departingFrom())
        second_destination = DestinationsLL().get_destination(flights[1].get_departingFrom())
        this_voyage = VoyagesLL().get_one_voyage(voyage_id)
        input_command = ''
        
        while input_command != 'q':
            Captain = EmployeesLL().get_one_employee(this_voyage.get_captain())
            if Captain == 'x':
                Captain_name = 'x'
            else:
                Captain_name = Captain.get_name()

            Copilot = EmployeesLL().get_one_employee(this_voyage.get_copilot())
            if Copilot == 'x':
                Copilot_name = 'x'
            else:
                Copilot_name = Copilot.get_name()
            
            FsManager = EmployeesLL().get_one_employee(this_voyage.get_FlightServiceManager())
            if FsManager == 'x':
                FsManager_name = 'x'
            else:
                FsManager_name = FsManager.get_name()
            
            Attendant = EmployeesLL().get_one_employee(this_voyage.get_flightAttendant())
            if Attendant == 'x':
                Attendant_name = 'x'
            else:
                Attendant_name = Attendant.get_name()
            
            self.header('Voyage: {}-{}'.format(flights[0].get_flightNumber(), flights[1].get_flightNumber()))
            print('Airplane: {}{}Captain: {}{}Copilot: {}'.format(this_voyage.get_planeInsignia(), ' '*6, Captain_name, ' '*6, Copilot_name))
            print('Flight Service Manager: {}{}Flight Attendant: {}\n'.format(FsManager_name, ' '*6, Attendant_name))
            print('{:^70}\n{:^70}\n'.format('Flight 1','-'*29))
            print('Destination: {} Airport{} Departure Location: {}\nArrival Time: {}{}Departure Time: {}\n'.format(first_destination.get_destination(), ' '*20, flights[0].get_departingFrom(), flights[0].get_arrival(), ' '*20, flights[0].get_departure()))
            print('Distance: {} km\nFlight time: {}{}Date: {}\nFlight number: {}'.format(second_destination.get_distance(), second_destination.get_flighttime(),' '*20, this_voyage.get_date(), flights[0].get_flightNumber()))
            print('\n{:^70}\n{:^70}\n'.format('Flight 2','-'*29))
            print('Destination: {} Airport{} Departure Location: {}\nArrival Time: {}{}Departure Time: {}\n'.format(second_destination.get_destination(), ' '*20, flights[1].get_departingFrom(), flights[1].get_arrival(), ' '*20, flights[1].get_departure()))
            print('Distance: {} km\nFlight time: {}{}Date: {}\nFlight number: {}'.format(second_destination.get_distance(), second_destination.get_flighttime(),' '*20, this_voyage.get_date(), flights[1].get_flightNumber()))
            print('\nb. Back one page')
            input_command = input('Enter input command: ')
            if input_command == 'b':
                VoyagesMenu().get_all_voyages()




    def get_all_voyages(self):
        input_command = ''
        while input_command != 'q':
            self.header('All Voyages')
            print('{:^5}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('ID', 'Insignia', 'Date', 'Destination', 'Captain', 'Copilot', 'Flight Service Manager', 'Flight Attendant'))
            print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('-'*5, '-'*5, '-'*5, '-'*5, '-'*5, '-'*5, '-'*5, '-'*5))
            all_voyages = VoyagesLL().get_voyages()
            
            counter = 0
            for line in all_voyages:
                Captain = EmployeesLL().get_one_employee(all_voyages[counter][4])
                if Captain == 'x':
                    Captain_name = 'x'
                else:
                    Captain_name = Captain.get_name()

                Copilot = EmployeesLL().get_one_employee(all_voyages[counter][5])
                if Copilot == 'x':
                    Copilot_name = 'x'
                else:
                    Copilot_name = Copilot.get_name()
                
                FsManager = EmployeesLL().get_one_employee(all_voyages[counter][6])
                if FsManager == 'x':
                    FsManager_name = 'x'
                else:
                    FsManager_name = FsManager.get_name()
                
                Attendant = EmployeesLL().get_one_employee(all_voyages[counter][7])
                if Attendant == 'x':
                    Attendant_name = 'x'
                else:
                    Attendant_name = Attendant.get_name()
                    
                line_counter = counter + 1
                print('{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^10}{:^10}{:^10}'.format(str(line_counter) + '.', all_voyages[counter][0], all_voyages[counter][1], all_voyages[counter][2], all_voyages[counter][3], Captain_name, Copilot_name, FsManager_name, Attendant_name))
                counter += 1
            print('')
            print('Back to Voyages....."b')
            input_command = input('Input Command: ').lower()
            for item in range(1,len(all_voyages) + 1):
                if input_command == str(item):
                    VoyagesMenu().get_voyage(all_voyages[item - 1][0])
                elif input_command == 'b':
                    VoyagesMenu().print_voyages_menu()
            
                


               

    def print_voyages_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header('Voyages')
            print('Menu\n-----\n1. Create Voyage\n2. Get All Voyages\n3. Update Voyage\n4. Back to Main menu\n')

            input_command = input('Input Command: ').lower()
            if input_command == '1':
                VoyagesMenu().create_voyage()
            elif input_command == '2':
                VoyagesMenu().get_all_voyages()
            elif input_command == '3':
                pass
            elif input_command == '4':
                pass