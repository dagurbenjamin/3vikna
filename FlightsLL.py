from LLAPI import LLAPI
from itertools import count


class FlightsLL():
    _ids = count(0)

    def __init__(self, flightdata = ""):
        self.id = next(self._ids)
        self.flightdata = flightdata


    def make_flightnumer(self, destination_data, flightdata):
        nan_air_letters = 'NA'
        destination_number = destination_data[-1]
        flight_number = '{}{}{}'.format(
            nan_air_letters, destination_number, self.id)
        flightdata.append(flight_number)
        print(flightdata)

    def get_past_flightsLL(self):
        past_flight_info = LLAPI().get_past_flights()
        print(past_flight_info)

    def get_upcoming_flights(self):
        pass



destination_data = ['GOH', 'Nuuk', 'Greenland', '1405',
                    'Kalli Lalli', '9119112', 'T03:00:00', '02']

flightdata = ['KEF', 'GOH', '2019-12-21T06:21:00', '2019-12-21T09:21:00']
x = FlightsLL().make_flightnumer(destination_data, flightdata)


flightdata_b = ['GOH', 'KEF', '2019-12-21T06:21:00', '2019-12-21T09:21:00']
y = FlightsLL().make_flightnumer(destination_data, flightdata_b)

past_flights = FlightsLL().get_past_flightsLL()

