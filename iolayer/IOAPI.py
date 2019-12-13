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

    def load_crew_from_file(self, ssn_toFind):
        return CrewIO().load_crew_from_file(ssn_toFind)

    def load_pilot_or_cabincrew(self, new_employee):
        return CrewIO().load_pilot_or_cabincrew(new_employee)

    def write_in_file(self, updated_employees_str):
        return CrewIO().write_in_file(updated_employees_str)

    def overwrite_crew_file(self, all_employees_list):
        return CrewIO().overwrite_crew_file(all_employees_list)

    def load_upcoming_flights_from_file(self, Voyage_to_find):
        return VoyagesIO().load_upcoming_flights_from_file(Voyage_to_find)

    def write_in_file_upcoming_flights(self, new_upcoming_flight):
        return VoyagesIO().write_in_file_past_flights(new_upcoming_flight)

    def overwrite_upcoming_flights_file(self, updated_upcoming_flights_str):
        return VoyagesIO().overwrite_upcoming_flights_file(updated_upcoming_flights_str)

    def load_past_flights_from_file(self, Voyage_to_find):
        return VoyagesIO().load_past_flights_from_file(Voyage_to_find)

    def write_in_file_past_flights(self, new_past_flight):
        return VoyagesIO().write_in_file_past_flights(new_past_flight)

    def load_voyages_from_file(self, voyageID):
        return VoyagesIO().load_voyages_from_file(voyageID)

    def write_in_voyages_flights(self, new_voyage):
        return VoyagesIO().write_in_voyages_flights(new_voyage)

    def overwrite_voyage_file(self, all_voyages_list):
        return VoyagesIO.overwrite_voyage_file(all_voyages_list)