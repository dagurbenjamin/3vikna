from iolayer.IOAPI import IOAPI

class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str
        self.IOAPI = IOAPI()

    def load_destinations(self, destination_id):
        return IOAPI().load_destinations(destination_id)

    def store_destination_to_file(self, new_destination_list):
        return IOAPI().store_destination_to_file(new_destination_list)

    def update_destination_and_overwrite(self, update_destination):
        return IOAPI().update_destination_and_overwrite(update_destination)

    def load_airplanes_from_file(self, planeID):
        return IOAPI().load_airplanes_from_file(planeID)

    def store_airplanes_to_file(self, new_airplane):
        return IOAPI().store_airplanes_to_file(new_airplane)

    def load_airplanesinfo(self, planeTypeId):
        return IOAPI().load_airplanesinfo(planeTypeId)

    def store_airplanesinfo_to_file(self, new_airplane_type):
        return IOAPI().store_airplanesinfo_to_file(new_airplane_type)

    def load_crew_from_file(self, ssn_toFind):
        return IOAPI().load_crew_from_file(ssn_toFind)

    def load_pilot_or_cabincrew(self, new_employee):
        return IOAPI().load_pilot_or_cabincrew(new_employee)

    def write_in_file(self, updated_employees_str):
        return IOAPI().write_in_file(updated_employees_str)

    def overwrite_crew_file(self, all_employees_list):
        return IOAPI().overwrite_crew_file(all_employees_list)

    def load_upcoming_flights_from_file(self, Voyage_to_find):
        return IOAPI().load_upcoming_flights_from_file(Voyage_to_find)

    def write_in_file_upcoming_flights(self, new_upcoming_flight):
        return IOAPI().write_in_file_past_flights(new_upcoming_flight)

    def overwrite_upcoming_flights_file(self, updated_upcoming_flights_str):
        return IOAPI().overwrite_upcoming_flights_file(updated_upcoming_flights_str)

    def load_past_flights_from_file(self, Voyage_to_find):
        return IOAPI().load_past_flights_from_file(Voyage_to_find)

    def write_in_file_past_flights(self, new_past_flight):
        return IOAPI().write_in_file_past_flights(new_past_flight)

    def load_voyages_from_file(self, voyageID):
        return IOAPI().load_voyages_from_file(voyageID)

    def write_in_voyages_flights(self, new_voyage):
        return IOAPI().write_in_voyages_flights(new_voyage)

    def overwrite_voyage_file(self, all_voyages_list):
        return IOAPI().overwrite_voyage_file(all_voyages_list)

