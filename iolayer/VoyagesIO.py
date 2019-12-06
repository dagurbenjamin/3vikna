import csv
from modules.pastflights import PastFlights
from modules.upcomingflights import UpcomingFlights


class VoyagesIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_upcoming_flights_from_file(self):
        allUpcoming_flights = []
        with open('./GognFraKennara/UpcomingFlights.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                upcomingFlight = UpcomingFlights(
                    row['flightNumber'], row['departingFrom'], row['arrivingAt'], row['departure'], row['arrival'])
                allUpcoming_flights.append(upcomingFlight)
        return allUpcoming_flights

    def write_in_file_upcoming_flights(self, new_upcoming_flight=''):
        f = open("UpcomingFlightsFile.csv", "a")
        f.write(new_upcoming_flight)
        f.close()

    def overwrite_upcoming_flights_file(self, updated_upcoming_flights_str=''):
        f = open("UpcomingFlightsFile.csv", "w")
        f.write(updated_upcoming_flights_str)
        f.close()

    def load_past_flights_from_file(self):
        allPast_flights = []
        with open('./GognFraKennara/PastFlights.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pastFlight = PastFlights(row['flightNumber'], row['departingFrom'], row['arrivingAt'], row['departure'],
                                         row['arrival'], row['aircraftID'], row['captain'], row['copilot'], row['fsm'], row['fa1'], row['fa2'])
                allPast_flights.append(pastFlight)
        return allPast_flights

    def write_in_file_past_flights(self, new_past_flight=''):
        f = open("PastFlightsFile.csv", "a")
        f.write(new_past_flight)
        f.close()
