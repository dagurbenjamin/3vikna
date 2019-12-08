import string
import os

class EmployeesMenu():

    def __init__(self):
        pass

    def header(self):
        print('*'*65,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n {}\n \n {} \n    ".format("*"*65, "{}Employees{}".format(" "*25, " "*30), "-"*65))


    def print_employees(self):
        self.header()
        print('Menu\n-----\n1. Create New Employee\n2. Get All Employees\n3. Update Employee\n4. Back to Main menu\n')
        input_command = ''
        while input_command != 'q':
            input_command = input('Input Command: ').lower()