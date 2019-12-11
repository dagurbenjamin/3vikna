from itertools import count
from iolayer.VoyagesIO import VoyagesIO


class FlightsLL():
    _ids = count(0)

    def __init__(self, flightdata=""):
        self.id = next(self._ids)
        self.flightdata = flightdata

    # def make_flightnumer(self, destination_data, flightdata):
    #     nan_air_letters = 'NA'
    #     destination_number = destination_data[-1]
    #     flight_number = '{}{}{}'.format(
    #         nan_air_letters, destination_number, self.id)
    #     flightdata.append(flight_number)
    #     print(flightdata)

    def get_past_flightsLL(self):
        past_flight_info = VoyagesIO().load_past_flights_from_file(Voyage_to_find)
        return past_flight_info

    def get_voyage_flights(self, Voyage_to_find):
        voyage_flights = VoyagesIO().load_upcoming_flights_from_file(Voyage_to_find)
        return voyage_flights
