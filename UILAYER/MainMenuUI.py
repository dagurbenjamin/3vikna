from UIMAIN import UIMAIN
from DestinationsMenuUI import DestinationsMenuUI

class Mainmenu():

    def __init__(self):
        pass
    def print_main_menu(self):
        print('****************************************************************')
        print('                                                                ')
        print('		        NaN Air                "q" - quitAndSave           ')
        print('                                                                ')
        print('****************************************************************')
        print('                                                                ')
        print('              Title                 Input Command               ')
        print('           ----------             -----------------             ')
        print('                                                                ')
        print('            Airplanes....................."1"                   ')
        print('                                                                ')
        print('            Destinations.................."2"                   ')
        print('                                                                ')
        print('            Employees....................."3"                   ')
        print('                                                                ')
        print('            Voyage........................"4"                   ')
        print('                                                                ')
        print('                                                                ')
        print('                                                                ')
        input_command = input("Enter input command: ")
        print('                                                                ')
        print('                                                                ')
        print('                                                                ')
        print('                                                                ')
        if input_command == '1':
            b = DestinationsMenuUI().print_all_destinations_menu()
        elif input_command == '2':
            b = DestinationsMenuUI().print_all_destinations_menu()



a = Mainmenu()
b = a.print_main_menu()
