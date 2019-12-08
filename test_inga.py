import csv
import os
from modules.aircraft.Aircraft import Aircraft
from modules.aircraft_type.Aircraft_type import Aircraft_type


class AircraftData(object):
    def __init__(self):
        pass

    @staticmethod
    def get_aircraft():
        try:
            with open("./data_files/AircraftType.csv") as file:
                csv_reader = csv.DictReader(file)
                aircrafts = []
                for line in csv_reader:
                    aircrafts.append(line)
                return aircrafts
            except Exception:
                return False
        
        @staticmethod
        def add_aircraft(aircraft):
            model = aircraft.get_model()
            


