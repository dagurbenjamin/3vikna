class DestinationsIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_destination_file(self, new_destination=''):
        f = open("DestinationsFile.csv", "a")
        f.write(new_destination)
        f.close()

    def overwrite_destination_file(self, updated_destination_str=''):
        f = open("DestinationsFile.csv", "w")
        f.write(updated_destination_str)
        f.close()