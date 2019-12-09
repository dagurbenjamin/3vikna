import csv
from modules.destinations import Destinations


class DestinationsIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_destination_from_file(self, destination_id):
        alldestinations = []
        with open('./data_files/Destinations.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if destination_id == '0':
                    destination = Destinations(row['id'], row['destination'], row['country'], row['distance'], row['contactname'],
                                               row['emergencynumber'], row['flighttime'], row['destinationnumber'])
                    alldestinations.append(destination)
                elif row['id'] == destination_id:
                    destination = Destinations(row['id'], row['destination'], row['country'], row['distance'],
                                               row['contactname'], row['emergencynumber'], row['flighttime'], row['destinationnumber'])
                    alldestinations.append(destination)
                    break
        return alldestinations

    def write_in_destination_file(self, new_destination=''):
        f = open("./data_files/Destinations.csv", "a")
        f.write(new_destination)
        f.close()

    def overwrite_destination_file(self, all_destinations_list):
        f = open("./data_files/Destinations.csv", "w")
        for line in all_destinations_list:
            str_line = ','.join(line)
            a_line = str_line + "\n"
            f.write(a_line)
        f.close()
