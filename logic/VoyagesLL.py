from IOLAYER.IOAPI import IOAPI
from iolayer.VoyagesIO import VoyagesIO


class VoyagesLL():
    def __init__(self, a_str):
        self.a_str = a_str

    def create_voyage(self, new_voyage_list):
        # id number, date, time, staff status
        new_voyage_list = ','.join(new_voyage_list)
        return new_voyage_list

    def get_voyage(self):
        # title = "id number, date, time, staff status"?

    def update_one_voyage(self, voyage_to_change, replacement_value, index_to_replace):
        allvoyage = VoyagesIO().load_voyages_from_file(voyage_to_change)
        for voyage in allvoyage:
            str_voyage = str(voyage)
            list_voyage = str_voyage.split(',')
            list_voyage[index_to_replace] = replacement_value
            EmployeesLL().change_the_big_list(employee_to_change_input, list_mem)
