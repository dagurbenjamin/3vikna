# from LLAPI import LLAPI
# from IOLAYER.IOAPI import IOAPI
from iolayer.CrewIO import CrewIO
from modules.Crew import Crew
from iolayer.VoyagesIO import VoyagesIO


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
        header = ['ssn', 'name', 'role', 'rank', 'crewlicense',
                  'address', 'phonenumber', 'email']
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
        return one_employee

    def get_pilots(self, p_or_c_input):
        pilots = CrewIO().load_pilot_or_cabincrew(p_or_c_input)
        return pilots
        
    def get_cabin_crew(self, p_or_c_input):
        cabin_crew = CrewIO().load_pilot_or_cabincrew(p_or_c_input)
        return cabin_crew

    def employees_working(self, inputt, voyageID='0'):
        x = VoyagesIO().load_voyages_from_file(voyageID)
        for line in x:
            if line.date == inputt:
                return line.captain, line.copilot, line.flightAttendant, line.FlightServiceManager, line.destination
            else:
                False
    
    def save_new_employee(self, employee):
        CrewIO().write_in_file(employee)

    def employees_not_working(inputt):
        list_of_non_workers = []
        list_of_workers = []
        x = VoyagesIO().load_voyages_from_file(voyageID="0")
        y = CrewIO().load_crew_from_file(ssn_toFind="0")
        for line in x:
            if line.date == inputt:
                list_of_workers.append(line.captain)
                list_of_workers.append(line.copilot)
                list_of_workers.append(line.FlightServiceManager)
                list_of_workers.append(line.flightAttendant)
        for line in y:
            list_of_non_workers.append(line.social)
        for employee in list_of_non_workers:
            if employee in list_of_workers:
                list_of_non_workers.remove(employee)

        return list_of_non_workers