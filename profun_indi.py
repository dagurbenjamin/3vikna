import csv
foo = open("UpcomingFlightsFile.csv", "r")
reader = csv.DictReader(foo)
for row in reader:
    print(row)
