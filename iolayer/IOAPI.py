import csv
import os


class IOAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_past_flights(self):
        load_past_flights = VoyagesIO().load_past_flights_from_file()
        return load_past_flights

    def store_past_flights_to_file(self, new_past_flight=''):
        store_past_flights = VoyagesIO().write_in_file_past_flights(new_past_flight)

    def load_upcoming_flights_from_file(self):
        load_upcoming_flights = VoyagesIO().load_upcoming_flights_from_file()
        return load_past_flights

    def store_upcoming_flights_to_file(self, new_upcoming_flight=''):
        store_upcoming_flights = VoyagesIO().write_in_file_upcoming_flights(new_upcoming_flight)

    def update_upcoming_flights_and_overwrite(self, updated_upcoming_flights_str=''):
        update_upcoming_flights = VoyagesIO().overwrite_upcoming_flights_file(
            updated_upcoming_flights_str)

    def load_destinations(self):
        load_destinations = DestinationsIO().load_destination_from_file()
        return load_destinations

    def store_destination_to_file(self, new_destination=''):
        store_destination = DestinationsIO().write_in_destination_file(new_destination)

    def update_destination_and_overwrite(self, updated_destination_str=''):
        update_destination = DestinationsIO(
        ).overwrite_destination_file(updated_destination_str)

    def load_airplanes_from_file(self, planeID):
        load_airplanes = AirplanesIO().load_airplanes_from_file()
        return load_airplanes

    def store_airplanes_to_file(self, new_airplane=''):
        store_airplanes = AirplanesIO().write_in_airplanes_file(new_airplane)

    def load_airplanesinfo(self):
        load_airplanes_info = AirplanesIO().load_airplanesinfo_from_file()
        return load_airplanes_info

    def store_airplanesinfo_to_file(self, new_airplane_type=''):
        store_airplanesinfo = AirplanesIO().write_in_airplanesinfo_file(new_airplane_type)

    def load_crew(self):
        load_crew = CrewIO().load_crew_from_file()
        return load_crew

    def store_crew_to_file(self, new_employee=''):
        store_crew = CrewIO().write_in_file(new_employee)

    def update_employee_and_overwrite(self, updated_employees_str=''):
        update_employee = CrewIO().overwrite_crew_file(updated_employees_str)
