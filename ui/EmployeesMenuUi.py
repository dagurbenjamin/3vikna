from iolayer.CrewIO import CrewIO
from modules.Crew import Crew
import string
import os

class EmployeesMenu():

    def __init__(self):
        self.employee = CrewIO()

    '''def select_employee(self, employee):
        while True:
            employee_id = self.'''

    def header(self):
        print('*'*65,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n {}\n \n {} \n    ".format("*"*65, "{}Employees{}".format(" "*25, " "*30), "-"*65))


    def print_employees_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header()
            print('Menu\n-----\n1. Create New Employee\n2. Get All Employees\n3. Update Employee\n4. Back to Main menu\n')

            input_command = input('Input Command: ').lower()
            if input_command == '1':
                pass
            elif input_command == '2':
                pass
            elif input_command == '3':
                pass
            elif input_command == '4':
                pass