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
            flight_2_departure_hour_int = departure_hour + flight_time_hour
            flight_2_departure_hour_str = str(flight_2_departure_hour_int + 1)
            flight_2_arrival_hour_str = str(int(flight_2_departure_hour_str) + 4)
            flight_2_departure_time = flight_2_departure_hour_str + new_voyage_list[3][2:]
            
            new_voyage_list.append(flight_2_departure_time)
            print('Departure time: {}'.format(flight_2_departure_time))

            input_command = new_voyage_list[4]
            new_voyage_list.append(input_command)
            print('Date: {}\n'.format(input_command))            
            airplane_check = VoyagesLL().is_airplane_available(new_voyage_list[4], new_voyage_list[0])
            if airplane_check:
                print('Menu\n{}'.format('-'*5))
                print('1. Save Voyage')
                print('2. Cancel')
                input_command = input('Input Command: ')
                if input_command == '1':
                    number_voyages = len(VoyagesLL().get_voyages()) + 1
                    save_voyage_list = [str(number_voyages),new_voyage_list[0],new_voyage_list[4],'x','x','x','x']
                    print(save_voyage_list)
                    VoyagesLL().create_voyage(save_voyage_list)
                    destination = DestinationsLL().get_destination(new_voyage_list[1])
                    flight_id = FlightsLL().get_voyage_flights('0')
                    flight_id = int(flight_id[-1].get_voyageID())
                    flight1_number = str(FlightsLL().make_flightnumer(destination, []))
                    flight2_number = str(FlightsLL().make_flightnumer(destination, []))                    
                    first_flight = [str(flight_id + 1),flight1_number,new_voyage_list[2],new_voyage_list[1],new_voyage_list[4] + 'T' + new_voyage_list[3], new_voyage_list[4] + 'T' + str(flight_2_departure_hour_int) + new_voyage_list[3][2:]]
                    second_flight = [str(flight_id + 1),flight2_number,new_voyage_list[1],new_voyage_list[2],new_voyage_list[4] + 'T' + flight_2_departure_hour_str + new_voyage_list[3][2:], new_voyage_list[4] + 'T' + flight_2_arrival_hour_str + new_voyage_list[3][2:]]
                    FlightsLL().create_upcoming_flight(first_flight)
                    FlightsLL().create_upcoming_flight(second_flight)
                    VoyagesMenu().get_voyage(str(number_voyages), str(number_voyages))
                elif input_command == '2':
                    VoyagesMenu().print_voyages_menu()
            else:
                while airplane_check == False:
                    print('Airplane is unavailable!\n{}'.format('-'*21))
                    input_command = input('Enter available airplane: ').upper()
                    print('')
                    new_voyage_list[0] = input_command
                    airplane_check = VoyagesLL().is_airplane_available(new_voyage_list[4], new_voyage_list[0])
                print('Menu\n{}'.format('-'*5))
                print('1. Save Voyage')
                print('2. Cancel\n')
                input_command = input('Input Command: ')
                if input_command == '1':
                    number_voyages = len(VoyagesLL().get_voyages()) + 1
                    save_voyage_list = [str(number_voyages),new_voyage_list[0],new_voyage_list[4],'x','x','x','x']
                    print(save_voyage_list)
                    VoyagesLL().create_voyage(save_voyage_list)
                    destination = DestinationsLL().get_destination(new_voyage_list[1])
                    flight_id = FlightsLL().get_voyage_flights('0')
                    flight_id = int(flight_id[-1].get_voyageID())
                    flight1_number = str(FlightsLL().make_flightnumer(destination, []))
                    flight2_number = str(FlightsLL().make_flightnumer(destination, []))                    
                    first_flight = [str(flight_id + 1),flight1_number,new_voyage_list[2],new_voyage_list[1],new_voyage_list[4] + 'T' + new_voyage_list[3], new_voyage_list[4] + 'T' + str(flight_2_departure_hour_int) + new_voyage_list[3][2:]]
                    second_flight = [str(flight_id + 1),flight2_number,new_voyage_list[1],new_voyage_list[2],new_voyage_list[4] + 'T' + flight_2_departure_hour_str + new_voyage_list[3][2:], new_voyage_list[4] + 'T' + flight_2_arrival_hour_str + new_voyage_list[3][2:]]
                    FlightsLL().create_upcoming_flight(first_flight)
                    FlightsLL().create_upcoming_flight(second_flight)
                    VoyagesMenu().get_voyage(str(number_voyages), str(number_voyages))
                elif input_command == '2':
                    VoyagesMenu().print_voyages_menu()


    def get_voyage(self, voyage_id, voyage2_id):
        flights_list = []
        flights = FlightsLL().get_voyage_flights(voyage_id)
        flights_list.append(flights)
        flight2 = FlightsLL().get_voyage_flights(voyage2_id)
        flights_list.append(flight2)
        print(flights_list)
        first_destination = DestinationsLL().get_destination(flights_list[0].get_departingFrom())
        second_destination = DestinationsLL().get_destination(flights_list[1].get_departingFrom())
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
            
            self.header('Voyage: {}-{}'.format(flights_list[0].get_flightNumber(), flights_list[1].get_flightNumber()))
            print('Airplane: {}{}Captain: {}{}Copilot: {}'.format(this_voyage.get_planeInsignia(), ' '*6, Captain_name, ' '*6, Copilot_name))
            print('Flight Service Manager: {}{}Flight Attendant: {}\n'.format(FsManager_name, ' '*6, Attendant_name))
            print('{:^70}\n{:^70}\n'.format('Flight 1','-'*29))
            print('Destination: {} Airport{} Departure Location: {}\nArrival Time: {}{}Departure Time: {}\n'.format(first_destination.get_destination(), ' '*20, flights_list[0].get_departingFrom(), flights_list[0].get_arrival(), ' '*20, flights_list[0].get_departure()))
            print('Distance: {} km\nFlight time: {}{}Date: {}\nFlight number: {}'.format(second_destination.get_distance(), second_destination.get_flighttime(),' '*20, this_voyage.get_date(), flights_list[0].get_flightNumber()))
            print('\n{:^70}\n{:^70}\n'.format('Flight 2','-'*29))
            print('Destination: {} Airport{} Departure Location: {}\nArrival Time: {}{}Departure Time: {}\n'.format(second_destination.get_destination(), ' '*20, flights_list[1].get_departingFrom(), flights_list[1].get_arrival(), ' '*20, flights_list[1].get_departure()))
            print('Distance: {} km\nFlight time: {}{}Date: {}\nFlight number: {}'.format(second_destination.get_distance(), second_destination.get_flighttime(),' '*20, this_voyage.get_date(), flights_list[1].get_flightNumber()))
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
            print('List voyages by day....."d"')
            print('List voyages by Week....."w"')
            input_command = input('Input Command: ').lower()
            for item in range(1,len(all_voyages) + 1):
                if input_command == str(item):
                    VoyagesMenu().get_voyage(all_voyages[item - 1][0], all_voyages[item][0])
                elif input_command == 'b':
                    VoyagesMenu().print_voyages_menu()
                elif input_command == 'd':
                    VoyagesMenu().list_voyages_by_day()
                elif input_command == 'w':
                    VoyagesMenu().list_voyages_by_week()


    def list_voyages_by_day(self):
        input_command = ''
        while input_command != 'q':
            self.header('List Voyages By Day')
            date = input('Enter date (yyyy-mm-dd): ').lower()
            voyages_that_day, staffed= VoyagesLL().list_voyages_by_day(date)
            VoyagesMenu().print_voyages_by_day(voyages_that_day, staffed, date)


    def print_voyages_by_day(self, voyages_that_day, staffed, date):
        input_command = ''
        while input_command != 'q':
            self.header(f'Voyages {date}')
            print('{:^6}{:^15}{:^15}{:^10}{:^12}'.format('ID', 'Insignia', 'Date', 'Destination', 'staffed'))
            print('{:^3}{:^13}{:^13}{:^9}{:^20}'.format('-'*5, '-'*5, '-'*5, '-'*5, '-'*5))
            counter = 0
            for voyage in voyages_that_day:
                print('{:^6}{:^13}{:^15}{:^20}{:^25}'.format(str(voyage[0]), voyage[1], voyage[2], voyage[3], staffed[counter]))
                counter += 1
            print('')
            print('Menu\n-----\n1. Back to All Voyages\n3. Back to Voyages menu\n')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                VoyagesMenu().get_all_voyages()
            elif input_command == '2':
                VoyagesMenu().print_voyages_menu()


    def list_voyages_by_week(self):
        input_command = ''
        while input_command != 'q':
            self.header('List Voyages week')
            weeknumber = int(input('Enter weeknumber: ').lower())
            all_voyages_in_that_week, staffed= VoyagesLL().list_voyages_by_week(weeknumber)
            VoyagesMenu().print_voyages_by_week(all_voyages_in_that_week, staffed, weeknumber)


    def print_voyages_by_week(self, all_voyages_in_that_week, staffed, weeknumber):
        input_command = ''
        while input_command != 'q':
            self.header(f'Voyages in week: {weeknumber}')
            print('{:^6}{:^15}{:^15}{:^10}{:^12}'.format('ID', 'Insignia', 'Date', 'Destination', 'staffed'))
            print('{:^3}{:^13}{:^13}{:^9}{:^20}'.format('-'*5, '-'*5, '-'*5, '-'*5, '-'*5))
            counter = 0
            for voyage in all_voyages_in_that_week:
                print('{:^6}{:^13}{:^15}{:^20}{:^25}'.format(str(voyage[0]), voyage[1], voyage[2], voyage[3], staffed[counter]))
                counter += 1
            print('')
            print('Menu\n-----\n1. Back to All Voyages\n3. Back to Voyages menu\n')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                VoyagesMenu().get_all_voyages()
            elif input_command == '2':
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
                VoyagesMenu().update_voyage_menu()
            elif input_command == '4':
                pass

    def update_voyage_menu(self):
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
            print('Choose Voyage to add staff:')
            input_command = input('Input Command: ').lower()
            for item in range(1,len(all_voyages) + 1):
                if input_command == str(item):
                    VoyagesMenu().what_to_update(all_voyages[item - 1][0])


    def what_to_update(self, voyage_id):
        input_command = ''
        while input_command != 'q':
            self.header('What do you want to update/add ?')
            print('')
            print('1. Captain\n2. Copilot\n3. Flight Service Manager\n4. Flight Attendant\n5. Back to Voyages Menu')
            print('\n\n\n')
            input_command = int(input('Input Command: ').lower())
            if input_command == 1:
                replacement_value = input('ssn for new Captain: ').lower()
                index_to_replace = input_command + 3
                x = VoyagesLL().update_one_voyage(voyage_id, replacement_value, index_to_replace)
                if x == 'False':
                    VoyagesMenu().employee_cant_be_added_to_voyage()
                else: 
                    VoyagesMenu().print_voyages_menu()
            elif input_command == 2:
                index_to_replace = input_command + 3
                replacement_value = input('ssn for new Copilot: ').lower()
                VoyagesLL().update_one_voyage(voyage_id, replacement_value, index_to_replace)
            elif input_command == 3:
                index_to_replace = input_command + 3
                replacement_value = input('ssn for new Flight Service Manager: ').lower()
                VoyagesLL().update_one_voyage(voyage_id, replacement_value, index_to_replace)
            elif input_command == 4:
                index_to_replace = input_command + 3
                replacement_value = input('ssn for new Flight Attendant: ').lower()
                VoyagesLL().update_one_voyage(voyage_id, replacement_value, index_to_replace)
            elif input_command == 5:
                VoyagesMenu().print_voyages_menu()


    def employee_cant_be_added_to_voyage(self):
        input_command = ''
        while input_command != 'q':
            self.header(' ')
            print('Employee could not be added to voyage,\nhe is registered to another voyage that same day')
            print('')
            print('')
            print('')
            print('Menu\n-----\n1. Go to All Voyages\n3. Back to Voyages menu\n')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                VoyagesMenu().get_all_voyages()
            elif input_command == '2':
                VoyagesMenu().print_voyages_menu()