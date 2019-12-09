
from iolayer.CrewIO import CrewIO
from iolayer.DestinationsIO import DestinationsIO
from iolayer.VoyagesIO import VoyagesIO
from modules.Crew import Crew
from datetime import datetime, date
from modules.Voyages import Voyages
import csv

def overwrite_in_right_rows():
    x = VoyagesIO().load_voyages_from_file()
    reader = csv.DictReader(x)
    for row in reader:



    for flights in x:
        flights = object(flights)

        print(flights)
        #flight_date = flights[3]
        #flight_date = flight_date.split("-")
        #print(flight_date)

        #flight_date2 = str(flight_date1)

        #flight_date3 = flight_date2.split("T")
        #print(flight_date3)
    #date_and_time = datetime(flight_date[3])
   # print(date_and_time)

overwrite_in_right_rows()



