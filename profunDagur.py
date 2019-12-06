import csv
from MODULES.Crew import Crew



def load_crew_from_file(self):
    with open('./data_files/CrewFile.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'],
                  row['address'], row['phonenumber'], row['email'], row['id'])