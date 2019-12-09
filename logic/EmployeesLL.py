# from LLAPI import LLAPI
# from IOLAYER.IOAPI import IOAPI
# from itertools import count
from modules.Crew import Crew
from iolayer.CrewIO import CrewIO


class EmployeesLL():

    def __init__(self, new_empl_list=[]):
        self.new_empl_list = new_empl_list

    def choose_employee_to_see(self, number, names_list):
        return names_list[number]

    def update_employee(self, employee_id_input):
        # get the crew file from data layer
        # þetta er þá óþarfi ekki satt?
        pass

    def change_value_for_one_employee(self, inputt, replacement_value, index_to_replace):
        x = CrewIO().load_crew_from_file(inputt)
        for member in x:
            str_member = str(member)
            list_mem = str_member.split(',')
            list_mem[index_to_replace] = replacement_value
        return list_mem

    def change_the_big_list(self, inputt, input_value, changed_employee):
        x = CrewIO().load_crew_from_file(input_value)
        a_list = []
        for member in x:
            str_member = str(member)
            list_member = str_member.split(',')
            if list_member[0] == inputt:
                list_member = changed_employee
            a_list.append(list_member)
        return a_list

    def get_all_employees(self):
        all_employees = CrewIO().load_crew_from_file('0')
        a_list = []
        for member in all_employees:
            str_member = str(member)
            list_employe = str_member.split(',')
            list_of_ssn_name_and_rank = list_employe[:3]
            a_list.append(list_of_ssn_name_and_rank)
        return list_of_ssn_name_and_rank
