class AirplanesIO(IOAPI):
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_airplanes_file(self, new_airplane=''):
        f = open("AirplanesFile.csv", "a")
        f.write(new_airplane)
        f.close()

    def write_in_airplanesinfo_file(self, new_airplane_type=''):
        f = open("AirplanesInfoFile.csv", "a")
        f.write(new_airplane_type)
        f.close()
