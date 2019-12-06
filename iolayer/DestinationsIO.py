class DestinationsIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_destination_from_file(self):
        alldestinations = []
        with open('./data_files/Destinations.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destination = Destinations(row['id'], row['destination'], row['country'], row['distance'], row['contactname'],
                                           row['emergencynumber'], row['flighttime'], row['destinationnumber'])
                alldestinations.append(destination)
        return alldestinations

    def write_in_destination_file(self, new_destination=''):
        f = open("DestinationsFile.csv", "a")
        f.write(new_destination)
        f.close()

    def overwrite_destination_file(self, updated_destination_str=''):
        f = open("DestinationsFile.csv", "w")
        f.write(updated_destination_str)
        f.close()
