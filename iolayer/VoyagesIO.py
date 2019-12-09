import csv
from modules.pastflights import PastFlights
from modules.upcomingflights import UpcomingFlights
from modules.Voyages import Voyages


class VoyagesIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_upcoming_flights_from_file(self):
        allUpcoming_flights = []
        with open('./data_files/UpcomingFlightsFile.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                upcomingFlight = UpcomingFlights(
                    row['voyageID'], row['flightNumber'], row['departingFrom'], row['arrivingAt'], row['departure'], row['arrival'])
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

    def load_voyages_from_file(self, voyageID):
        all_voyages = []
        with open('./data_files/VoyagesFile.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if voyageID == '0'
                voyage = Voyages(row['voyageID'], row['planeInsignia'], row['date'], row['captain'], row['copilot'],
                                 row['FlightServiceManager'], row['flightAttendant'])
                all_voyages.append(voyage)
                elif row['voyageID'] == voyageID:
                voyage = Voyages(row['voyageID'], row['planeInsignia'], row['date'], row['captain'],
                                 row['copilot'], row['FlightServiceManager'], row['flightAttendant'])
                all_voyages.append(voyage)
                break
        return all_voyages

    def write_in_voyages_flights(self, new_voyage=''):
        f = open("./data_files/VoyagesFile.csv", "a")
        f.write(new_voyage)
        f.close()

    def overwrite_voyage_file(self, all_voyages_list):
        f = open("./data_files/CrewFile.csv", "w")
        for line in all_voyages_list:
            str_voyage = ','.join(line)
            a_voyage = str_voyage + "\n"
            f.write(a_voyage)
            f.close()
