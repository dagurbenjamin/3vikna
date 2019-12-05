import csv


class IOAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_past_flights_from_file(self):
        fileStream_past_flights = open("PastFlights.csv", "r")
        return fileStream_past_flights

    def store_past_flights_to_file(self, new_past_flight=''):
        c = VoyagesIO().write_in_file_past_flights(new_past_flight)

    def load_upcoming_flights_from_file(self):
        fileStream_upcoming_flights = open("UpcomingFlights.csv", "r")
        return fileStream_upcoming_flights

    def store_upcoming_flights_to_file(self, new_upcoming_flight=''):
        d = VoyagesIO().write_in_file_upcoming_flights(new_upcoming_flight)

    def update_upcoming_flights_and_overwrite(self, updated_upcoming_flights_str=''):
        b = VoyagesIO().overwrite_upcoming_flights_file(updated_upcoming_flights_str)

    def load_destination_from_file(self):
        fileStream_destinations = open("DestinationsFile.csv", "r")
        return fileStream_destinations

    def store_destination_to_file(self, new_destination=''):
        d = DestinationsIO().write_in_destination_file(new_destination)

    def update_destination_and_overwrite(self, updated_destination_str=''):
        b = DestinationsIO().overwrite_destination_file(updated_destination_str)

    def load_airplanes_from_file(self, planeID):
        fileStream_aircraft = open("Aircraft.csv", "r")
        return fileStream_aircraft

    def store_airplanes_to_file(self, new_airplane=''):
        g = AirplanesIO().write_in_airplanes_file(new_airplane)

    def load_airplanesinfo_from_file(self):
        fileStream_airplanesinfo = open("AirplanesInfoFile.csv", "r")
        return fileStream_airplanesinfo

    def store_airplanesinfo_to_file(self, new_airplane_type=''):
        s = AirplanesIO().write_in_airplanesinfo_file(new_airplane_type)

    def load_crew_from_file(self):
        with open('CrewFile.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['first_name'], row['last_name'])

    def store_crew_to_file(self, new_employee=''):
        b = CrewIO().write_in_file(new_employee)

    def update_employee_and_overwrite(self, updated_employees_str=''):
        b = CrewIO().overwrite_crew_file(updated_employees_str)


class CrewIO(IOAPI):
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_file(self, new_crew_member=''):
        f = open("CrewFile.csv", "a")
        f.write(new_crew_member)
        f.close()

    def overwrite_crew_file(self, updated_employees_str=''):
        f = open("CrewFile.csv", "w")
        f.write(updated_employees_str)
        f.close()


class AirplanesIO(IOAPI):
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_airplanes_file(self, new_airplane=''):
        f = open("AirplanesFile.csv", "a")
        f.write(new_airplane)
        f.close()

    def write_in_airplanesinfo_file(self, new_airplane_type=''):
        f = open("AirplanesInfoFile.csv", "a")
        f.write(new_airplane_type)
        f.close()


class DestinationsIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_destination_file(self, new_destination=''):
        f = open("DestinationsFile.csv", "a")
        f.write(new_destination)
        f.close()

    def overwrite_destination_file(self, updated_destination_str=''):
        f = open("DestinationsFile.csv", "w")
        f.write(updated_destination_str)
        f.close()


class VoyagesIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_file_past_flights(self, new_past_flight=''):
        f = open("PastFlightsFile.csv", "a")
        f.write(new_past_flight)
        f.close()

    def write_in_file_upcoming_flights(self, new_upcoming_flight=''):
        f = open("UpcomingFlightsFile.csv", "a")
        f.write(new_upcoming_flight)
        f.close()

    def overwrite_upcoming_flights_file(self, updated_upcoming_flights_str=''):
        f = open("UpcomingFlightsFile.csv", "w")
        f.write(updated_upcoming_flights_str)
        f.close()


x = IOAPI().load_crew_from_file()
