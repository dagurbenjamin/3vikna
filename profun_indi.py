
# from iolayer.AirplanesIO import AirplanesIO
# from iolayer.CrewIO import CrewIO
# from iolayer.DestinationsIO import DestinationsIO
# from iolayer.VoyagesIO import VoyagesIO
# from modules.Crew import Crew
from logic.EmployeesLL import EmployeesLL
from iolayer.DestinationsIO import DestinationsIO
from logic.DestinationsLL import DestinationsLL
from iolayer.VoyagesIO import VoyagesIO
# x = AirplanesIO().load_airplanes_from_file()
# y = AirplanesIO().load_airplanesinfo_from_file()
# a = CrewIO().load_crew_from_file()
# b = DestinationsIO().load_destination_from_file()
# c = VoyagesIO().load_past_flights_from_file()
# d = VoyagesIO().load_upcoming_flights_from_file()

from iolayer.CrewIO import CrewIO
from logic.VoyagesLL import VoyagesLL
from logic.AirplanesLL import AirplanesLL

# employee_to_change_ssn_input = '2211658134'
# replacement_value = 'Captain'
# input_index = 2
# index_to_replace = input_index + 1
# changed_employee = EmployeesLL().change_value_for_one_employee(
#     employee_to_change_ssn_input, replacement_value, index_to_replace)


# destination_to_change_input = 'LYR'
# replacement_value = 'Doddi'
# input_index = 1
# index_to_replace = input_index + 3
# changed_destination = DestinationsLL().update_destination(
#     destination_to_change_input, replacement_value, index_to_replace)


# number_voyage_to_change = '3'
# replacement_value = '2910858778'
# replacement_value = '1900769521'
# replacement_value = '2200763823'
# replacement_value = '3003962187'
# input_index = 1
# index_to_replace = input_index + 3
# changed_voyage = VoyagesLL().update_one_voyage(
#     number_voyage_to_change, replacement_value, index_to_replace)
# print(changed_voyage)
# Voyage_to_find = '2'
# x = VoyagesIO().load_upcoming_flights_from_file(Voyage_to_find)
# print(x)

# voyageID = '0'

# x = VoyagesLL().is_voyage_fully_staffed(voyageID)

# date = '2019-12-21'


# list_voyages_by_day(date)
# date_list = []
# year = str(input('input year: '))
# date_list.append(year)
# month = str(input('input month: '))
# date_list.append(month)
# day = str(input('input day: '))
# date_list.append(day)
# print(date_list)


# def list_voyages_by_week(week_start, the_input='0'):
#     all_voyages = VoyagesIO().load_voyages_from_file(the_input)
#     for line in all_voyages:
#         str_voyage = str(line)
#         list_voyage = str_voyage.split(',')
#         if list_voyage[2] == date:
#             str_voyage = str(line)
#             list_voyage = str_voyage.split(',')
#             print(line)
#             if list_voyage[4] == 'x' or list_voyage[5] == 'x' or list_voyage[6] == 'x' or list_voyage[7] == 'x':
#                 print('Voyage is not fully staffed!')
#             else:
#                 print('Voyage is fully staffed!')


# weeknumber = int(input('input weeknumber: '))
# # x = VoyagesLL().list_voyages_by_week(weeknumber)
1
# employee = '2504939263'


# EmployeesLL().get_employee_week_schedule(weeknumber, employee)

date = '2019-12-20'
# plane_insignia = 'TF-EPG'
# x = AirplanesLL().is_airplane_available(date, plane_insignia)
# if x:
#     print('it returned true')
# else:
#     print('it returned false')

x = EmployeesLL().employees_not_working(date)
print(x)
