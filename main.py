from ui.DestinationsMenuUI import DestinationsMenu
from ui.AirplanesMenuUI import AirplanesMenu
from ui.EmployeesMenuUi import EmployeesMenu
from ui.VoyagesMenuUI import VoyagesMenu
import os
# import ctypes
# import msvcrt
# import subprocess

# kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
# user32 = ctypes.WinDLL('user32', use_last_error=True)

# SW_MAXIMIZE = 3

# kernel32.GetConsoleWindow.restype = wintypes.HWND
# kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
# kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
# user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

#


def fullscreen():
    pass


def airplanes_main():
    AirplanesMenu().print_airplanes_menu()


def destination_main():
    DestinationsMenu().print_destinations_menu()


def employees_main():
    EmployeesMenu().print_employees_menu()


def voyages_main():
    VoyagesMenu().print_voyages_menu()


def asciiplane():
    print('                                  |')
    print('                                  |')
    print('                            --====|====--')
    print('                                  |')
    print('')
    print('                              .-"""""-.')
    print("                            .'_________'.")
    print('                           /_/_|__|__|_\_\ ')
    print("                          ;'-._       _.-';")
    print('    {}'.format(
        " ,--------------------|    `-. .-'    |--------------------,"))
    print("      ``''--..__    ___   ;       '       ;   ___    __..--''``")
    print('                `"-// \\\.._\             /_..// \\\-"`')
    print("                   \\\_//    '._       _.'    \\\_//")
    print('                    `"`        ``---``        `"`')
    print('')


# def maximize_console(lines=None):
#     fd = os.open('CONOUT$', os.O_RDWR)
#     try:
#         hCon = msvcrt.get_osfhandle(fd)
#         max_size = kernel32.GetLargestConsoleWindowSize(hCon)
#         if max_size.X == 0 and max_size.Y == 0:
#             raise ctypes.WinError(ctypes.get_last_error())
#     finally:
#         os.close(fd)
#     cols = max_size.X
#     hWnd = kernel32.GetConsoleWindow()
#     if cols and hWnd:
#         if lines is None:
#             lines = max_size.Y
#         else:
#             lines = max(min(lines, 9999), max_size.Y)
#         subprocess.check_call('mode.com con cols={} lines={}'.format(
#             cols, lines))
#         user32.ShowWindow(hWnd, SW_MAXIMIZE)


def main():
    # os.system('cls')
    # maximize_console()
    # asciiplane()
    input_command = ''
    while input_command != 'q':
        print('*'*75, '\n')
        print('{}NaN Air   ''\033[91m                 {} \033[00m'.format(' '*31,
                                                                          '"q" - quitAndSave\n'))
        print('*'*75, '\n')
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
