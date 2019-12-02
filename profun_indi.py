import csv


class IOAPI():
    def __init__(self, a_str):
        self.a_str = a_str

    def load_past_flights_from_file(self):
        fileStream_past_flights = open("PastFlightsFile.csv", "r")
        return fileStream_past_flights

    def store_past_flights_to_file(self, a_str):
        c = VoyagesIO(self.a_str)
        c.write_in_file_past_flights(self.a_str)

    def load_upcoming_flights_from_file(self):
        fileStream_upcoming_flights = open("UpcomingFlightsFile.csv", "r")
        return fileStream_upcoming_flights

    def store_upcoming_flights_to_file(self, a_str):
        d = VoyagesIO(self.a_str)
        d.write_in_file_upcoming_flights(self.a_str)

    def load_destination_from_file(self, destination):
        fileStream_destinations = open("DestinationsFile.csv", "r")
        return fileStream_destinations

    def store_destination_to_file(self):
        pass

    def load_airplanes_from_file(self, planeID):
        fileStream_aircraft = open("Aircraft.csv", "r")
        return fileStream_aircraft

    def store_airplanes_to_file(self):
        pass

    def load_airplanetypes_from_file(self):
        pass

    def store_airplanetypes_to_file(self):
        pass

    def load_crew_from_file(self):
        fileStream_crew = open("Crew.csv", "r")
        return fileStream_crew

    def store_crew_to_file(self, a_str):
        b = CrewIO(self.a_str)
        b.write_in_file(self.a_str)


class CrewIO(IOAPI):
    def __init__(self, a_str):
        self.a_str = a_str

    def write_in_file(self, a_str):
        f = open("CrewFile.csv", "a")
        f.write(a_str)
        f.close()


class AirplanesIO(IOAPI):
    def __init__(self, newAirplane):
        self.newAirplane = newAirplane

    def write_in_file(self, newAirplane):
        f = open("AirplanesFile.csv", "a")
        f.write(newAirplane)
        f.close()


class DestinationsIO(IOAPI):
    def __init__(self, newDestination):
        self.newDestination = newDestination

    def write_in_file(self, newDestination):
        f = open("DestinationsFile.csv", "a")
        f.write(newDestination)
        f.close()


class VoyagesIO():
    def __init__(self, a_str):
        self.a_str = a_str

    def write_in_file_past_flights(self, a_str):
        f = open("PastFlightsFile.csv", "a")
        f.write(a_str)
        f.close()

    def write_in_file_upcoming_flights(self, a_str):
        f = open("UpcomingFlightsFile.csv", "a")
        f.write(a_str)
        f.close()


def main():
    newEmployee = 'New employee \n'
    a = IOAPI(newEmployee)
    a.store_crew_to_file(newEmployee)

    pastFlight = "i am a past flight \n"
    x = IOAPI(pastFlight)
    x.store_past_flights_to_file(pastFlight)

    UpcomingFlight = "i am a upcoming flight \n"
    y = IOAPI(UpcomingFlight)
    y.store_upcoming_flights_to_file(UpcomingFlight)


main()
