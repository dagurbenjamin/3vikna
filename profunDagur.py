from iolayer.AirplanesIO import AirplanesIO
from iolayer.CrewIO import CrewIO
from iolayer.DestinationsIO import DestinationsIO
from iolayer.VoyagesIO import VoyagesIO
from modules.Crew import Crew


inputt = "2211658134"
replacement_value = "Captain"
input_index = 2
index_to_replace = input_index + 1

x = CrewIO().load_crew_from_file(inputt)
for member in x:
    string_member = str(member)
    list_member = string_member.split(",")

