import csv
import os
from iolayer.AirplanesIO import AirplanesIO
from iolayer.CrewIO import CrewIO
from iolayer.DestinationsIO import DestinationsIO
from iolayer.VoyagesIO import VoyagesIO


class IOAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str
        self.destIO = DestinationsIO()
        self.airpIO = AirplanesIO()
        self.voyaIO = VoyagesIO()
        self.crewIO = CrewIO()

    def load_past_flights(self):
        load_past_flights = VoyagesIO().load_past_flights_from_file(Voyage_to_find='0')
        return load_past_flights

    def store_past_flights_to_file(self, new_past_flight=''):
        store_past_flights = VoyagesIO().write_in_file_past_flights(new_past_flight)
        return store_past_flights

    def load_upcoming_flights_from_file(self):
        load_upcoming_flights = VoyagesIO().load_upcoming_flights_from_file(Voyage_to_find="0")
        return load_upcoming_flights

    def store_upcoming_flights_to_file(self, new_upcoming_flight=''):
        store_upcoming_flights = VoyagesIO().write_in_file_upcoming_flights(new_upcoming_flight)
        return store_upcoming_flights

    def update_upcoming_flights_and_overwrite(self, updated_upcoming_flights_str=''):
        update_upcoming_flights = VoyagesIO().overwrite_upcoming_flights_file(
            updated_upcoming_flights_str)
        return update_upcoming_flights

    def load_destinations(self, destination_id):
        return DestinationsIO().load_destination_from_file(destination_id)


    def store_destination_to_file(self, new_destination_list):
        return DestinationsIO().write_in_destination_file(new_destination_list)


    def update_destination_and_overwrite(self, destination_bla):
        return DestinationsIO().overwrite_destination_file(destination_bla)


    def load_airplanes_from_file(self, planeID):
        return AirplanesIO().load_airplanes_from_file(planeID)

    def store_airplanes_to_file(self, new_airplane):
        return AirplanesIO().write_in_airplanes_file(new_airplane)

    def load_airplanesinfo(self, planeTypeId):
        return AirplanesIO().load_airplanesinfo_from_file(planeTypeId)

    def store_airplanesinfo_to_file(self, new_airplane_type):
        return AirplanesIO().write_in_airplanesinfo_file(new_airplane_type)


    def load_crew(self):
        load_crew = CrewIO().load_crew_from_file(ssn_toFind="0")
        return load_crew

    def store_crew_to_file(self, new_employee=''):
        store_crew = CrewIO().write_in_file(new_employee)
        return store_crew

    def update_employee_and_overwrite(self, updated_employees_str=''):
        update_employee = CrewIO().overwrite_crew_file(updated_employees_str)
        return update_employee