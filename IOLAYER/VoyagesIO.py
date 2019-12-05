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
