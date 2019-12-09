
from iolayer.AirplanesIO import AirplanesIO
from iolayer.CrewIO import CrewIO
from iolayer.DestinationsIO import DestinationsIO
from iolayer.VoyagesIO import VoyagesIO
from modules.Crew import Crew
from logic.EmployeesLL import EmployeesLL

#x = IOAPI().load_destination_from_file()
# print('')
# b = IOAPI().load_crew_from_file()
# c = Crew("", "")
# IOAPI().store_crew_to_file(c)


# x = AirplanesIO().load_airplanes_from_file()
# y = AirplanesIO().load_airplanesinfo_from_file()
# a = CrewIO().load_crew_from_file()
# b = DestinationsIO().load_destination_from_file()
# c = VoyagesIO().load_past_flights_from_file()
# d = VoyagesIO().load_upcoming_flights_from_file()


# inputt = '2211658134'
# replacement_value = 'Captain'
# input_index = 2
# index_to_replace = input_index + 1
# changed_employee = EmployeesLL().change_value_for_one_employee(
#     inputt, replacement_value, index_to_replace)
# input_value = '0'
# all_employees_list = EmployeesLL().change_the_big_list(
#     inputt, input_value, changed_employee)
# print(all_employees_list)


def get_all_employees():
    all_employees = CrewIO().load_crew_from_file('0')
    a_list = []
    for member in all_employees:
        str_member = str(member)
        list_member = str_member.split(',')
        what_i_want = list_member[:3]
        a_list.append(what_i_want)
    print(a_list)


get_all_employees()
