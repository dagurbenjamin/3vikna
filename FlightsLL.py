from itertools import count


class Flights():
    _ids = count(1)

    def __init__(self, flightdata):
        self.id = next(self._ids)
        self.flightdata = flightdata

    def make_flightnumer(self, flightdata, destination_data):
        NaN_air_letters = 'NA'
        destination_number = destination_data[-1]
        flight_number = '{}{}{}'.format(
            NaN_air_letters, destination_number, self.id)


destination_data = ['GOH', 'Nuuk', 'Greenland', '1405',
                    'Kalli Lalli', '9119112', 'T03:00:00', '02']

flightdata = ['KEF', 'GOH', '2019-12-21T06:21:00', '2019-12-21T09:21:00']
x = Flights(flightdata)
x.make_flightnumer(flightdata, destination_data)


flightdata_b = ['GOH', 'KEF', '2019-12-21T06:21:00', '2019-12-21T09:21:00']
y = Flights(flightdata_b)
y.make_flightnumer(flightdata_b, destination_data)
