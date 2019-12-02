import csv


class IOAPI():
    def __init__(self, newEmployee):
        self.newEmployee = newEmployee

    def loadVoyageFromFile(self, voyageID):
        pass

    def storeVoyageToFile(self):
        pass

    def loadDestinationFromFile(self, destination):
        fileStream_destinations = open("Destinations.csv", "r")
        return fileStream_destinations

    def storeDestinationToFile(self):
        pass

    def loadAirplanesFromFile(self, planeID):
        fileStream_aircraft = open("Aircraft.csv", "r")
        return fileStream_aircraft

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
    def __init__(self, newAirplane):
        self.newAirplane = newAirplane

    def write_in_file(self, newAirplane):
        f = open("AirplanesFile.csv", "a")
        f.write(newAirplane)
        f.close()


class DestinationsIO(IOAPI):
    def __init__(self, newDestination):
        self.newDestination = newDestination

    def write_in_file(self, newDestination):
        f = open("DestinationsFile.csv", "a")
        f.write(newDestination)
        f.close()


class VoyagesIO():
    def __init__(self, newvoyage):
        self.newvoyage = newvoyage

    def write_in_file(self, newvoyage):
        f = open("VoyagesFile.csv", "a")
        f.write(newvoyage)
        f.close()


def main():
    newEmployee = 'New employee \n'
    a = IOAPI(newEmployee)
    a.storeCrewToFile(newEmployee)


main()
