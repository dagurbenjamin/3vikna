from logic.VoyagesLL import VoyagesLL
from modules.Voyages import Voyages
from logic.FlightsLL import FlightsLL
from logic.DestinationsLL import DestinationsLL
from logic.EmployeesLL import EmployeesLL
import string
import os

class VoyagesMenu():

    def __init__(self):
        pass

    def header(self, title):
        print('*'*95,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n{}\n \n {} \n    ".format("*"*95, "{}{}{}".format(" "*23, title, " "*30), "-"*65))

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
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                VoyagesMenu().get_voyage(all_voyages[0][0])
                


               

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