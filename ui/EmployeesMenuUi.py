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
        print('*'*95,'\n')
        print('                          NaN Air   ''\033[91m            {} \033[00m'.format('"q" - quitAndSave'))
        print("\n{}\n \n {} \n    ".format("*"*95, "{}{}{}".format(" "*23, title, " "*30), "-"*65))
    
    def get_employee(self, ssn):
        one_employee = EmployeesLL().get_one_employee(ssn)
        input_command = ''
        while input_command != 'q':
            self.header(one_employee.get_name())
            print('\n{:^15}{:^32}{:^23}'.format('Role','Rank','License'))
            print('{:^15}{:^32}{:^25}'.format('-'*6,'-'*8,'-'*12))
            print('{:^15}{:^33}{:^23}\n'.format(one_employee.get_role(),one_employee.get_rank(),one_employee.get_license()))
            print('{:^13}{:^38}{:^14}{:^14}'.format('SSN','Address','Phone number','Email'))
            print('{:^15}{:^32}{:^22}{}'.format('-'*10,'-'*9,'-'*12,'-'*5))
            print('{:^15}{:^36}{:^15}{}\n'.format(one_employee.get_social(),one_employee.get_address(),one_employee.get_phone(),one_employee.get_email()))
            print('1. Get employees week schedule')
            print('\n\n2. Back to Main menu\n3. Back to All Employees\n4. Back to All Pilots\n')
            
            input_command = input("Input command: ").lower()
            if input_command == '1':
                EmployeesMenu().get_week_schedule(ssn, one_employee.get_name())
            elif input_command == '2':
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
            print('Get Cabin Crew......."c"')
            print('All Employees...."b"')
            input_command = input('Enter input command: ').lower()
            for item in range(1,len(pilots) + 1):
                if input_command == str(item):
                    EmployeesMenu().get_employee(pilots[item - 1].get_social())
                elif input_command == 'p':
                    EmployeesMenu().get_cabin_crew('CabinCrew')
                elif input_command == 'b':
                    EmployeesMenu().get_all_employees()
           
    
    def get_cabin_crew(self, p_or_c_input):
        cabin_crew = EmployeesLL().get_cabin_crew(p_or_c_input)
        input_command = ''
        while input_command != 'q':
            self.header('Cabin Crew')
            print('\n{:^22}{:^23}{:^15}'.format('Name','SSN','Rank',))
            print('{:^22}{:^25}{:^8}'.format('-'*6,'-'*8,'-'*12,))
            counter = 0
            for line in cabin_crew:
                line_counter = counter + 1
                print('{:^5}{:^20}{:^25}{:^15}'.format(str(line_counter) + '.', cabin_crew[counter].get_name() , cabin_crew[counter].get_social() , cabin_crew[counter].get_rank()))
                counter += 1
            print('')
            print('Get pilots......."p"')
            print('All Employees...."b"')
            input_command = input('Enter input command: ').lower()
            for item in range(1,len(cabin_crew) + 1):
                if input_command == str(item):
                    EmployeesMenu().get_employee(cabin_crew[item - 1][0])
                elif input_command == 'p':
                    EmployeesMenu().get_all_pilots('Pilot')
                elif input_command == 'b':
                    EmployeesMenu().get_all_employees()


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
            print('Get pilots......."p"')
            print('Get cabin crew..."c"')
            input_command = input("Input command: ").lower()
            for item in range(1,len(all_employees) + 1):
                if input_command == str(item):
                    EmployeesMenu().get_employee(all_employees[item - 1][0])
                elif input_command == 'p':
                    EmployeesMenu().get_all_pilots('Pilot')
                elif input_command == 'c':
                    EmployeesMenu().get_cabin_crew('Cabincrew')

            
            
            
            


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
            print('{:^13}{:^38}{:^14}{:^16}'.format('SSN','Address','Phone number','Email'))
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

    def update_this_employee(self, ssn):
        one_employee = EmployeesLL().get_one_employee(ssn)
        input_command = ''
        while input_command != 'q':
            self.header(one_employee.get_name())
            print('\n{:^15}{:^32}{:^23}'.format('Role','Rank','License'))
            print('{:^15}{:^32}{:^25}'.format('-'*6,'-'*8,'-'*12))
            print('{:^15}{:^33}{:^23}\n'.format(one_employee.get_role(),one_employee.get_rank(),one_employee.get_license()))
            print('{:^13}{:^38}{:^14}{:^14}'.format('SSN','Address','Phone number','Email'))
            print('{:^15}{:^32}{:^22}{}'.format('-'*10,'-'*9,'-'*12,'-'*5))
            print('{:^15}{:^36}{:^15}{}\n'.format(one_employee.get_social(),one_employee.get_address(),one_employee.get_phone(),one_employee.get_email()))
            print('What would you like to update?')
            print('{}\n1. Role\n2. Rank\n3. License\n4. Address\n5. Phone number\n6. Email\n7. Back one page'.format('-'*6))
            
            input_command = input("Input command: ").lower()
            if input_command == '1':
                input_command = input('New role of employee: ')
                one_employee.set_role(input_command)
                one_employee_list = str(one_employee).split(',')
                EmployeesLL().change_the_big_list(one_employee.get_social(), one_employee_list)
            elif input_command == '2':
                input_command = input('New rank of employee: ')
                one_employee.set_rank(input_command)
                one_employee_list = str(one_employee).split(',')
                EmployeesLL().change_the_big_list(one_employee.get_social(), one_employee_list)
                input_command = input('Role of Employee: ')
            elif input_command == '3':
                input_command = input('New License of Employee: ')
                one_employee.set_license(input_command)
                one_employee_list = str(one_employee).split(',')
                EmployeesLL().change_the_big_list(one_employee.get_social(), one_employee_list)
                continue
            elif input_command == '4':
                input_command = input('New Address of Employee: ')
                one_employee.set_address(input_command)
                one_employee_list = str(one_employee).split(',')
                EmployeesLL().change_the_big_list(one_employee.get_social(), one_employee_list)
                input_command = input('Role of Employee: ')
            elif input_command == '5':
                input_command = input('New Phone number of Employee: ')
                one_employee.set_phone(input_command)
                one_employee_list = str(one_employee).split(',')
                EmployeesLL().change_the_big_list(one_employee.get_social(), one_employee_list)
                input_command = input('Role of Employee: ')
            elif input_command == '6':
                input_command = input('New Email of Employee: ')
                one_employee.set_rank(input_command)
                one_employee_list = str(one_employee).split(',')
                EmployeesLL().change_the_big_list(one_employee.get_social(), one_employee_list)
                input_command = input('Role of Employee: ')
            elif input_command == '7':
                EmployeesMenu().update_employee()

    
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
            print('Employees menu..."b"')
            print('Which employee would you like to update?')
            input_command = input("Input command: ").lower()
            for item in range(1,len(all_employees) + 1):
                if input_command == str(item):
                    EmployeesMenu().update_this_employee(all_employees[item - 1][0])
                elif input_command == 'b':
                    EmployeesMenu().print_employees_menu()
            
            

    def print_employees_menu(self):
        input_command = ''
        while input_command != 'q':
            self.header('Employees')
            print('Menu\n-----\n1. Create New Employee\n2. Get All Employees\n3. Update Employee\n4. Crew schedules\n5.Back to Main menu\n')
            input_command = input('Input Command: ').lower()
            if input_command == '1':
                EmployeesMenu().create_new_employee()
            elif input_command == '2':
                EmployeesMenu().get_all_employees()
            elif input_command == '3':
                EmployeesMenu().update_employee()
            elif input_command == '4':
                EmployeesMenu().print_employees_working_a_certain_day()
            elif input_command == '5':
                pass

    def get_week_schedule(self, ssn, employee_name):
        input_command = ''
        while input_command != 'q':
            self.header(f'Week schedule for: {employee_name}')
            print('Enter week number: ')
            weeknumber = int(input())
            week_schedule = EmployeesLL().get_employee_week_schedule(weeknumber, ssn)
            EmployeesMenu().print_week_schedule(week_schedule, ssn)


    def print_week_schedule(self, week_schedule, ssn):
        for voyage in week_schedule:
            print('{:^73}'.format(voyage[2]))
            print('{:^72}'.format('-'*18))
            print('   VoyageID: {}{} planeInsignia: {}{} destination: {}'.format(voyage[0],' '*6, voyage[1],' '*6, voyage[3]))
            print('')
        print('Menu\n-----\n1. Back to employee\n2. Back to All Employees\n3. Back to Main menu\n')
        input_command = input('Input Command: ').lower()
        if input_command == '1':
            EmployeesMenu().get_employee(ssn)
        elif input_command == '2':
            EmployeesMenu().get_all_employees()
        elif input_command == '3':
            pass

    def print_employees_working_a_certain_day(self):
        input_command = ''
        while input_command != 'q':
            self.header('Crew schedules')
            print('')
            input_command = input('Enter Date: ').lower()
            list_of_non_workers = EmployeesLL().employees_not_working(input_command)
            print('')
            print('{:^30}'.format(f'All employees Not working'))
            print('{:^29}'.format('-'*12))
            print('{:^85}'.format(f'All employees working'))
            print('{:^83}'.format('-'*12))
            for ssn in list_of_non_workers:
                employee = EmployeesLL().get_one_employee(ssn)
                employee_name = employee.get_name()
                print('{:^33}'.format(f'{employee_name}'))
            list_of_workers = EmployeesLL().employees_working(input_command)
            print(list_of_workers)
        print('Menu\n-----\n1. Back to All Employees\n3. Back to Main menu\n')
        if input_command == '1':
            EmployeesMenu().get_all_employees()
        elif input_command == '2':
            pass