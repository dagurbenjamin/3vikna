from ui.DestinationsMenuUI import DestinationsMenu
from ui.AirplanesMenuUI import AirplanesMenu
from ui.EmployeesMenuUi import EmployeesMenu
from ui.VoyagesMenuUI import VoyagesMenu
import os
import ctypes

def fullscreen():
    pass

def airplanes_main():
    airplanes = AirplanesMenu()
    airplanes.print_airplanes_menu()


def destination_main():
    destination = DestinationsMenu()
    destination.print_destinations_menu()

def employees_main():
    employees = EmployeesMenu()
    employees.print_employees_menu()

def voyages_main():
    voyages = VoyagesMenu()
    voyages.print_voyages_menu()


def main():
    input_command = ''
    while input_command != 'q':
        print('*'*65,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print('\n','*'*65,'\n')
        print('Main menu\n----------\n1. Airplanes\n2. Destinations\n3. Employees\n4. Voyage\n')
        input_command = input('Input Command: ').lower()
        if input_command == '1':
            airplanes_main()
        elif input_command == '2':
            destination_main()
        elif input_command == '3':
            employees_main()
        elif input_command == '4':
            voyages_main()
            

main()