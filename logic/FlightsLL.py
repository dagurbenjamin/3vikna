from LLAPI import LLAPI
from itertools import count


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
        past_flight_info = LLAPI().get_past_flights()
        print(past_flight_info)

    def get_voyage_flights(self):
        voyage_flights = LLAPI().load_upcoming_flights_from_file(Voyage_to_find)
        return voyage_flights
