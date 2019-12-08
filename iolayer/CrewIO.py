import csv
from modules.Crew import Crew


class CrewIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_crew_from_file(self):
        allcrew = []
        with open('./data_files/CrewFile.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row[ssn] == ssn_toFind):
                    employee = Crew(row['ssn'], row['name'], row['role'], row['rank'], row['licence'],
                                    row['address'], row['phonenumber'], row['email'], row['id'])
                    allcrew.append(employee)
                    break
        return allcrew  # samt bara 1

    def write_in_file(self, new_crew_member=''):
        f = open("CrewFile.csv", "a")
        f.write(new_crew_member)
        f.close()

    def overwrite_crew_file(self, updated_employees_str=''):
        f = open("CrewFile.csv", "w")
        f.write(updated_employees_str)
        f.close()
