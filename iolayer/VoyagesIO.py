class VoyagesIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_upcoming_flights_from_file(self):
        allUpcoming_flights = []
        with open('./data_files/Aircraft.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                upcomingFlight = Aircraft(
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
        with open('./data_files/Aircraft.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pastFlight = Aircraft(row['flightNumber'], row['departingFrom'], row['arrivingAt'], row['departure'],
                                      row['arrival'], row['aircraftID'], row['captain'], row['copilot'], row['fsm'], row['fa1'], row['fa2'])
                allPast_flights.append(pastFlight)
        return allPast_flights

    def write_in_file_past_flights(self, new_past_flight=''):
        f = open("PastFlightsFile.csv", "a")
        f.write(new_past_flight)
        f.close()
