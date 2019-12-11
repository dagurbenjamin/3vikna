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
        print('*'*75,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n{}\n \n {} \n    ".format("*"*75, "{}{}{}".format(" "*23, title, " "*30), "-"*65))
    
    def get_employee(self, ssn):
        one_employee = EmployeesLL().get_one_employee(ssn)
        print(one_employee)
        input_command = ''
        while input_command != 'q':
            self.header(one_employee.get_name())
            print('\n{:^15}{:^32}{:^23}'.format('Role','Rank','License'))
            print('{:^15}{:^32}{:^25}'.format('-'*6,'-'*8,'-'*12))
            print('{:^15}{:^33}{:^23}\n'.format(one_employee.get_role(),one_employee.get_rank(),one_employee.get_license()))
            print('{:^13}{:^38}{:^14}{}'.format('SSN','Address','Phone number','Email'))
            print('{:^15}{:^32}{:^22}{}'.format('-'*10,'-'*9,'-'*12,'-'*5))
            print('{:^15}{:^36}{:^15}{}\n'.format(one_employee.get_social(),one_employee.get_address(),one_employee.get_phone(),one_employee.get_email()))
            print('\n\n1. Back to Main menu\n2. Back to All Employees\n3. Back to All Pilots\n')
            
            input_command = input("Input command: ").lower()
            if input_command == '2':
                EmployeesMenu().get_all_employees()
            elif input_command == '3':
                EmployeesMenu().get_all_pilots('Pilot')


    def get_all_pilots(self, p_or_c_input):
        pilots = EmployeesLL().get_pilots(p_or_c_input)
        input_command = ''
        while input_command != 'q':
            self.header('Pilots')
            print('\n{:^22}{:^23}{:^15}{:^20}'.format('Name','SSN','Rank','License'))
            print('{:^22}{:^25}{:^8}{:^18}'.format('-'*6,'-'*8,'-'*12,'-'*12))
            counter = 0
            for line in pilots:
                line_counter = counter + 1
                print('{:^5}{:^17}{:^25}{:^15}{:^15}'.format(str(line_counter) + '.', pilots[counter].get_name() , pilots[counter].get_social() , pilots[counter].get_rank() , pilots[counter].get_license()))
                counter += 1
            print('')
            input_command = input('Enter input command: ').lower()
            if input_command == '1':
                EmployeesMenu().get_employee(pilots[0].get_social())
            elif input_command == '2':
                EmployeesMenu().get_employee(pilots[1].get_social())
            elif input_command == '3':
                EmployeesMenu().get_employee(pilots[2].get_social())
            elif input_command == '4':
                EmployeesMenu().get_employee(pilots[3].get_social())
            elif input_command == '5':
                EmployeesMenu().get_employee(pilots[4].get_social())
            elif input_command == '6':
                EmployeesMenu().get_employee(pilots[5].get_social())
            elif input_command == '7':
                EmployeesMenu().get_employee(pilots[6].get_social())
            elif input_command == '8':
                EmployeesMenu().get_employee(pilots[7].get_social())
            elif input_command == '9':
                EmployeesMenu().get_employee(pilots[8].get_social())
            elif input_command == '10':
                EmployeesMenu().get_employee(pilots[9].get_social())
            elif input_command == '11':
                EmployeesMenu().get_employee(pilots[10].get_social())
            elif input_command == '12':
                EmployeesMenu().get_employee(pilots[11].get_social())



            




    
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
            print('Get all pilots......"Pilots"')
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
            elif input_command == 'pilots':
                EmployeesMenu().get_all_pilots('Pilot')

    def create_new_employee(self):
        self.header('Create New Employee')
        input_command = ''
        new_employee = ''
        new_employee_list = []
        while input_command != 'q':
            input_command = input('SSN of Employee: ')
            new_employee_list.append(input_command)
            input_command = input('Name of Employee: ')
            new_employee_list.append(input_command)
            input_command = input('Role of Employee: ')
            new_employee_list.append(input_command)
            input_command = input('Rank of Employee: ')
            new_employee_list.append(input_command)
            input_command = input('License of Employee: ')
            new_employee_list.append(input_command)
            input_command = input('Address of Employee: ')
            new_employee_list.append(input_command)
            input_command = input('Phone number of Employee: ')
            new_employee_list.append(input_command)
            input_command = input('Email of Employee: ')
            new_employee_list.append(input_command)
            self.header(new_employee_list[1])
            print('\n{:^15}{:^32}{:^23}'.format('Role','Rank','License'))
            print('{:^15}{:^32}{:^25}'.format('-'*6,'-'*8,'-'*12))
            print('{:^15}{:^33}{:^23}\n'.format(new_employee_list[2],new_employee_list[3],new_employee_list[4]))
            print('{:^13}{:^38}{:^14}{:^14}'.format('SSN','Address','Phone number','Email'))
            print('{:^15}{:^32}{:^22}{}'.format('-'*10,'-'*9,'-'*12,'-'*12))
            print('{:^15}{:^36}{:^15}{}\n'.format(new_employee_list[0],new_employee_list[5],new_employee_list[6],new_employee_list[7]))
            print('\nIs this correct?\n-----\n1. Yes\n2. No\n')
            input_command = input('Input Command: ')  
            if input_command == '1':
                new_employee = ','.join([str(elem) for elem in new_employee_list]) 
                EmployeesLL().save_new_employee(new_employee)
                print('\nEmployee added!\n')
                EmployeesMenu().get_all_employees()
            elif input_command == '2':
                continue
    def update_this_employee(self):
        pass

    
    def update_employee(self):
        input_command = ''
        while input_command != 'q':
            self.header('Update Employees')
            print('{:^20}{:^20}{:^18}'.format('SSN', 'Name', 'Role'))
            print('{:^20}{:^19}{:^20}'.format('-'*10, '-'*17, '-'*10))
            all_employees = EmployeesLL().get_all_employees()
            counter = 0
            for line in all_employees:
                line_counter = counter + 1
                print('{:^5}{:^5}{:^30}{:^10}'.format(str(line_counter) + '.' ,all_employees[counter][0], all_employees[counter][1], all_employees[counter][2]))
                counter += 1
            print('')
            print('Which employee would you like to update?"')
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
                EmployeesMenu().create_new_employee()
            elif input_command == '2':
                EmployeesMenu().get_all_employees()
            elif input_command == '3':
                EmployeesMenu().update_employee()
            elif input_command == '4':
                pass
    
