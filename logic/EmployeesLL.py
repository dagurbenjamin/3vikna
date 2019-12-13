
from logic.LLAPI import LLAPI
#from iolayer.CrewIO import CrewIO
from modules.Crew import Crew
#from iolayer.VoyagesIO import VoyagesIO
from logic.VoyagesLL import VoyagesLL


class EmployeesLL():
    def __init__(self, new_empl_list=[]):
        self.new_empl_list = new_empl_list
        self.LLAPI = LLAPI()

    def change_value_for_one_employee(self, employee_to_change_ssn_input, replacement_value, index_to_replace):
        allCrew = LLAPI().load_crew_from_file(employee_to_change_ssn_input)
        for member in allCrew:
            str_member = str(member)
            list_mem = str_member.split(',')
            list_mem[index_to_replace] = replacement_value
            EmployeesLL().change_the_big_list(employee_to_change_ssn_input, list_mem)

# changing the file_contents to overwrite again with updated employee
    def change_the_big_list(self, employee_to_change_ssn_input, changed_employee, input_value='0'):
        x = LLAPI().load_crew_from_file(input_value)
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
        LLAPI().overwrite_crew_file(a_list)

    def get_all_employees(self):
        all_employees = LLAPI().load_crew_from_file('0')
        a_list = []
        for member in all_employees:
            str_member = str(member)
            list_employee = str_member.split(',')
            list_of_ssn_name_and_rank = list_employee[:3]
            a_list.append(list_of_ssn_name_and_rank)
        return a_list

    def get_one_employee(self, ssn):
        if ssn == 'x':
            return 'x'
        else:
            one_employee = LLAPI().load_crew_from_file(ssn)
            if one_employee == []:
                return 'x'
            else:
                return one_employee

    def get_pilots(self, p_or_c_input):
        pilots = LLAPI().load_pilot_or_cabincrew(p_or_c_input)
        return pilots

    def get_cabin_crew(self, p_or_c_input):
        cabin_crew = LLAPI().load_pilot_or_cabincrew(p_or_c_input)
        return cabin_crew

    def employees_working(self, date_inputt, voyageID='0'):
        all_voyages = LLAPI().load_voyages_from_file(voyageID)
        employees_working_list = []
        destinations_list = []
        for line in all_voyages:
            if line.date == date_inputt:
                employees_list = []
                if line.captain != 'x':
                    employees_list.append(line.captain)
                if line.copilot != 'x':
                    employees_list.append(line.copilot)
                if line.flightAttendant != 'x':
                    employees_list.append(line.flightAttendant)
                if line.FlightServiceManager != 'x':
                    employees_list.append(line.FlightServiceManager)
                employees_working_list.append(employees_list)
                destinations_list.append(line.destination)
        return employees_working_list, destinations_list

    def save_new_employee(self, employee):
        LLAPI().write_in_file(employee)

    def employees_not_working(self, day_inputt):
        list_of_non_workers = []
        list_of_workers = []
        x = LLAPI().load_voyages_from_file(voyageID="0")
        all_employees = LLAPI().load_crew_from_file(ssn_toFind="0")
        for line in x:
            if line.date == day_inputt:
                list_of_workers.append(line.captain)
                list_of_workers.append(line.copilot)
                list_of_workers.append(line.FlightServiceManager)
                list_of_workers.append(line.flightAttendant)
        for line in all_employees:
            if line.social not in list_of_workers:
                list_of_non_workers.append(line.social)
        return list_of_non_workers

    def get_employee_week_schedule(self, weeknumber, employee):
        all_voyages_that_week = VoyagesLL().list_voyages_by_week(weeknumber)
        employees_week_schedule = []
        for voyage in all_voyages_that_week:
            for element in voyage:
                if element == employee:
                    employees_week_schedule.append(voyage)
        if len(employees_week_schedule) == 0:
            print('employee is not working this week')
        else:
            return employees_week_schedule

    def get_all_employees_with_all_informations(self):
        all_employees = LLAPI().load_crew_from_file('0')
        all_employees_list = []
        for member in all_employees:
            str_member = str(member)
            list_employee = str_member.split(',')
            all_employees_list.append(list_employee)
        return all_employees_list
