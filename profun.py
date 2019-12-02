import csv


class IOAPI():
    def __init__(self, foo):
        self.foo = foo

    def storeCrewToFile(self, foo):
        f = open("CrewFile.csv", "w+")
        f.write(foo)
        f.close()


foo = 'Hello world'
a = IOAPI(foo)
a.storeCrewToFile(foo)


# def main():
#     boo = IOAPI(foo)
