import csv
from modules.aircraft import Aircraft
from modules.aircraft_type import Aircraft_type


class AirplanesIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_airplanesinfo_from_file(self, planeTypeId):
        allAirplaneInfo = []
        with open('./data_files/AircraftType.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if planeTypeId == '0'
                airplaneinfo = Aircraft_type(row['planeTypeId'], row['manufacturer'], row['model'], row['capacity'], row['emptyWeight'],
                                             row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
                allAirplaneInfo.append(airplaneinfo)
                elif row['planeTypeId'] == planeTypeId:
                info_about_one_airplane = Aircraft_type(row['planeTypeId'], row['manufacturer'], row['model'], row['capacity'], row['emptyWeight'],
                                                        row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
                return info_about_one_airplane
                break
        return allAirplaneInfo

    def write_in_airplanesinfo_file(self, new_airplane_type=''):
        f = open("./data_files/AirplanesInfoFile.csv", "a")
        f.write(new_airplane_type)
        f.close()

    def load_airplanes_from_file(self, planeInsignia_toFind):
        allAircrafts = []
        with open('./data_files/Aircraft.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if planeInsignia_toFind == '0':
                    airplane = Aircraft(
                        row['planeInsignia'], row['planeTypeId'])
                    allAircrafts.append(airplane)
                elif row['planeInsignia'] == planeInsignia_toFind:
                    airplane = Aircraft(
                        row['planeInsignia'], row['planeTypeId'])
                    allAircrafts.append(airplane)
                    break
        return allAircrafts

    def write_in_airplanes_file(self, new_airplane=''):
        f = open("./data_files/AirplanesFile.csv", "a")
        f.write(new_airplane)
        f.close()
