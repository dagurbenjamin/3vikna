import csv


class IOAPI():
    def __init__(self, newEmployee):
        self.newEmployee = newEmployee

    def loadVoyageFromFile(self, voyageID):
        pass

    def storeVoyageToFile(self):
        pass

    def loadDestinationFromFile(self, destination):
        pass

    def storeDestinationToFile(self):
        pass

    def loadAirplanesFromFile(self, planeID):
        pass

    def storeAirplanesToFile(self):
        pass

    def loadCrewFromFile(self):
        fileStream_crew = open("Crew.csv", "r")
        return fileStream_crew

    def storeCrewToFile(self, newEmployee):
        b = CrewIO(self.newEmployee)
        b.write_in_file(self.newEmployee)


class CrewIO(IOAPI):
    def __init__(self, newEmployee):
        self.newEmployee = newEmployee

    def write_in_file(self, newEmployee):
        f = open("CrewFile.csv", "a")
        f.write(newEmployee)
        f.close()


class AirplanesIO(IOAPI):
    def __init__(self):
        pass

    def write_in_file(self, newAirplane):
        f = open("AirplanesFile.csv", "a")
        f.write(newAirplane)
        f.close()


class DestinationsIO():
    def __init__(self):
        pass

    def write_in_file(self, newDestination):
        f = open("CrewFile.csv", "a")
        f.write(newDestination)
        f.close()


class VoyagesIO():
    def __init__(self):
        pass

    def write_in_file(self, newvoyage):
        f = open("CrewFile.csv", "a")
        f.write(newvoyage)
        f.close()


newEmployee = 'New employee \n'
a = IOAPI(newEmployee)
a.storeCrewToFile(newEmployee)
