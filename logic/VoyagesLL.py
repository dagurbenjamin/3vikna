
from iolayer.VoyagesIO import VoyagesIO
import datetime
import time


class VoyagesLL():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def create_voyage(self, new_voyage_list):
        # id number, date, time, staff status
        new_voyage_list = ','.join(new_voyage_list)
        return new_voyage_list

    def update_one_voyage(self, number_voyage_to_change, replacement_value, index_to_replace):
        one_voyage = VoyagesIO().load_voyages_from_file(number_voyage_to_change)
        for voyage in one_voyage:
            str_voyage = str(voyage)
            list_voyage = str_voyage.split(',')
            employees_working_same_day = EmployeesLL(
            ).employees_working(list_voyage[2])
            if replacement_value in employees_working_same_day:
                return print('cant add employee, hes working this day')
            else:
                list_voyage[index_to_replace] = replacement_value
                VoyagesLL().change_the_big_voyage_list(number_voyage_to_change, list_voyage)

    def change_the_big_voyage_list(self, number_voyage_to_change, new_list_voyage, input_value='0'):
        all_voyages = VoyagesIO().load_voyages_from_file(input_value)
        all_voyages_list = []
        for voyage in all_voyages:
            str_voyage = str(voyage)
            list_voyage = str_voyage.split(',')
            if list_voyage[0] == number_voyage_to_change:
                list_voyage = new_list_voyage
            all_voyages_list.append(list_voyage)
        header = ['voyageID', 'planeInsignia', 'date', 'destination', 'captain',
                  'copilot', 'FlightServiceManager', 'flightAttendant']
        all_voyages_list.insert(0, header)
        VoyagesIO().overwrite_voyage_file(all_voyages_list)

    def is_voyage_fully_staffed(self, voyageID):
        voyages = VoyagesIO().load_voyages_from_file(voyageID)
        for line in voyages:
            str_voyage = str(line)
            list_voyage = str_voyage.split(',')
            if list_voyage[4] == 'x' or list_voyage[5] == 'x' or list_voyage[6] == 'x' or list_voyage[7] == 'x':
                return print('Voyage is not fully staffed!')
            else:
                return print('Voyage is fully staffed!')
    
    def get_voyages(self):
        all_voyages = VoyagesIO().load_voyages_from_file('0')
        a_list = []
        for voyage in all_voyages:
            str_voyage = str(voyage)
            list_voyage = str_voyage.split(',')
            list_of_voyages = list_voyage
            a_list.append(list_of_voyages)
        return a_list

    def get_one_voyage(self, voyageID):
        one_employee = VoyagesIO().load_voyages_from_file('')
        return one_employee
