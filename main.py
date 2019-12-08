from ui.DestinationsMenuUI import DestinationsMenu
from ui.AirplanesMenuUI import AirplanesMenu
from ui.EmployeesMenuUi import EmployeesMenu
from ui.VoyagesMenuUI import VoyagesMenu
import os
import ctypes

'''def open_fullscreen():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')

    SW_MAXIMIZE = 3

    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_MAXIMIZE)'''

def airplanes_main():
    airplanes = AirplanesMenu()
    airplanes.print_airplanes()


def destination_main():
    destination = DestinationsMenu()
    destination.print_destinations()

def employees_main():
    employees = EmployeesMenu()
    employees.print_employees()

def voyages_main():
    voyages = VoyagesMenu()
    voyages.print_voyages()


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