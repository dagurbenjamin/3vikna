import csv
from modules.aircraft import Aircraft
from modules.aircraft_type import Aircraft_type


class AirplanesIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_airplanesinfo_from_file(self):
        allAirplaneInfo = []
        with open('./data_files/AircraftType.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                airplaneinfo = Aircraft_type(row['planeTypeId'], row['manufacturer'], row['model'], row['capacity'], row['emptyWeight'],
                                             row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
                allAirplaneInfo.append(airplaneinfo)
        return allAirplaneInfo

    def write_in_airplanesinfo_file(self, new_airplane_type=''):
        f = open("AirplanesInfoFile.csv", "a")
        f.write(new_airplane_type)
        f.close()

    def load_airplanes_from_file(self):
        allAircrafts = []
        with open('./data_files/Aircraft.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                airplane = Aircraft(row['planeInsignia'], row['planeTypeId'])
                allAircrafts.append(airplane)
        return allAircrafts

    def write_in_airplanes_file(self, new_airplane=''):
        f = open("AirplanesFile.csv", "a")
        f.write(new_airplane)
        f.close()
