from logic.EmployeesLL import EmployeesLL
from modules.Crew import Crew
import string
import os

class EmployeesMenu():

    def __init__(self):
        self.employee = EmployeesLL()

    '''def select_employee(self, employee):
        while True:
            employee_id = self.'''

    def header(self, title):
        print('*'*65,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n {}\n \n {} \n    ".format("*"*65, "{}{}{}".format(" "*23, title, " "*30), "-"*65))
    
    def get_employee(self, ssn):
        one_employee = EmployeesLL().get_one_employee(ssn)        
        input_command = ''
        while input_command != 'q':
            self.header(one_employee.get_name())
            print('\n{:^15}{:^32}{:^23}'.format('Role','Rank','License'))
            print('{:^15}{:^32}{:^25}'.format('-'*6,'-'*8,'-'*12))
            print('{:^15}{:^33}{:^23}\n'.format(one_employee.get_role(),one_employee.get_rank(),one_employee.get_license()))
            print('{:^13}{:^38}{:^14}'.format('SSN','Address','Phone number'))
            print('{:^15}{:^32}{:^22}'.format('-'*10,'-'*9,'-'*12))
            print('{:^15}{:^36}{:^15}\n'.format(one_employee.get_social(),one_employee.get_address(),one_employee.get_phone()))
            print('\n\n1. Back to Main menu\n2. Back to Submenu\n3. Back one page\n')
            
            input_command = input("Input command: ").lower()
            if input_command == '3':
                a = EmployeesMenu().get_all_employees()



    
    def get_all_employees(self):
        input_command = ''
        while input_command != 'q':
            self.header('All Employees')
            print('{:^20}{:^20}{:^18}'.format('SSN', 'Name', 'Role'))
            print('{:^20}{:^19}{:^20}'.format('-'*10, '-'*17, '-'*10))
            all_employees = EmployeesLL().get_all_employees()
            counter = 0
            for line in all_employees:
                line_counter = counter + 1
                print('{:^5}{:^5}{:^30}{:^10}'.format(str(line_counter) + '.' ,all_employees[counter][0], all_employees[counter][1], all_employees[counter][2]))
                counter += 1
            print('')
            input_command = input("Input command: ").lower()
            
            if input_command == '1':
                EmployeesMenu().get_employee(all_employees[0][0])
            elif input_command == '2':
                EmployeesMenu().get_employee(all_employees[1][0])
            elif input_command == '3':
                EmployeesMenu().get_employee(all_employees[2][0])
            elif input_command == '4':
                EmployeesMenu().get_employee(all_employees[3][0])
            elif input_command == '5':
                EmployeesMenu().get_employee(all_employees[4][0])
            elif input_command == '6':
                EmployeesMenu().get_employee(all_employees[5][0])
            elif input_command == '7':
                EmployeesMenu().get_employee(all_employees[6][0])
            elif input_command == '8':
                EmployeesMenu().get_employee(all_employees[20][0])



            

                
                






    def print_employees_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header('Employees')
            print('Menu\n-----\n1. Create New Employee\n2. Get All Employees\n3. Update Employee\n4. Back to Main menu\n')

            input_command = input('Input Command: ').lower()
            if input_command == '1':
                pass
            elif input_command == '2':
                a = EmployeesMenu().get_all_employees()
            elif input_command == '3':
                pass
            elif input_command == '4':
                pass
    
