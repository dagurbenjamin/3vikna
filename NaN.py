import csv


class IOAPI():
    def __init__(self, foo):
        self.foo = foo

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

    def storeCrewToFile(self, foo):
        a = CrewIO(foo)
        a.write_in_file(foo)


class CrewIO(IOAPI):
    def __init__(self, foo):
        self.foo = foo

    def write_in_file(self, foo):
        f = open("CrewFile.csv", "a")
        f.write(foo)
        f.close()


def main():
    foo = 'Hello world \n'
    a = IOAPI(foo)
    a.storeCrewToFile(foo)
