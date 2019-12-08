
from iolayer.AirplanesIO import AirplanesIO
from iolayer.CrewIO import CrewIO
from iolayer.DestinationsIO import DestinationsIO
from iolayer.VoyagesIO import VoyagesIO
from modules.Crew import Crew

#x = IOAPI().load_destination_from_file()
# print('')
# b = IOAPI().load_crew_from_file()
# c = Crew("", "")
# IOAPI().store_crew_to_file(c)


#x = AirplanesIO().load_airplanes_from_file()
#y = AirplanesIO().load_airplanesinfo_from_file()
# a = CrewIO().load_crew_from_file()
# b = DestinationsIO().load_destination_from_file()
# c = VoyagesIO().load_past_flights_from_file()
# d = VoyagesIO().load_upcoming_flights_from_file()


# inputt = 'Cabincrew'
# x = CrewIO().load_pilot_or_cabincrew(inputt)
# print(x)
# a = []

# for crew in x:
#     b = []
#     b.append(crew)
#     a.append(b)
# print(a)

inputtt = '0'
y = AirplanesIO().load_airplanes_from_file(inputtt)
print(y)
