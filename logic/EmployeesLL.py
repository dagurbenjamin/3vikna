# from LLAPI import LLAPI
# from IOLAYER.IOAPI import IOAPI
from iolayer.CrewIO import CrewIO
from modules.Crew import Crew


class EmployeesLL():

    def __init__(self, new_empl_list=[]):
        self.new_empl_list = new_empl_list

    def change_value_for_one_employee(self, employee_to_change_ssn_input, replacement_value, index_to_replace):
        allCrew = CrewIO().load_crew_from_file(employee_to_change_input)
        for member in allCrew:
            str_member = str(member)
            list_mem = str_member.split(',')
            list_mem[index_to_replace] = replacement_value
            EmployeesLL().change_the_big_list(employee_to_change_ssn_input, list_mem)

    def change_the_big_list(self, employee_to_change_ssn_input, changed_employee, input_value='0'):
        x = CrewIO().load_crew_from_file(input_value)
        a_list = []
        for member in x:
            str_member = str(member)
            list_member = str_member.split(',')
            if list_member[0] == employee_to_change_ssn_input:
                list_member = changed_employee
            a_list.append(list_member)
        header = ['ssn', 'name', 'role', 'rank', 'licence',
                  'address', 'phonenumber', 'email', 'id']
        a_list.insert(0, header)
        CrewIO().overwrite_crew_file(a_list)

    def get_all_employees(self):
        all_employees = CrewIO().load_crew_from_file('0')
        a_list = []
        for member in all_employees:
            str_member = str(member)
            list_employee = str_member.split(',')
            list_of_ssn_name_and_rank = list_employee[:3]
            a_list.append(list_of_ssn_name_and_rank)
        return a_list

    def get_one_employee(self, ssn):
        one_employee = CrewIO().load_crew_from_file(ssn)
        print(type(one_employee), 'her')
        return one_employee
