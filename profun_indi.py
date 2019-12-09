
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

# employee_to_change_input = '2211658134'
# replacement_value = 'Captain'
# input_index = 2
# index_to_replace = input_index + 1
# changed_employee = EmployeesLL().change_value_for_one_employee(
#     employee_to_change_input, replacement_value, index_to_replace)


# destination_to_change_input = 'LYR'
# replacement_value = 'Doddi'
# input_index = 1
# index_to_replace = input_index + 3
# changed_destination = DestinationsLL().update_destination(
#     destination_to_change_input, replacement_value, index_to_replace)

VoyagesIO().load_voyages_from_file()
