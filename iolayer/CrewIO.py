import csv

# from logic.EmployeesLL import EmployeesLL
from modules.Crew import Crew


class CrewIO():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def load_crew_from_file(self, ssn_toFind):
        allcrew = []
        with open('./data_files/CrewFile.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if ssn_toFind == '0':
                    employee = Crew(row['ssn'], row['name'], row['role'], row['rank'], row['crewlicense'],
                                    row['address'], row['phonenumber'], row['email'])
                    allcrew.append(employee)
                elif row['ssn'] == ssn_toFind:
                    employee = Crew(row['ssn'], row['name'], row['role'], row['rank'], row['crewlicense'],
                                    row['address'], row['phonenumber'], row['email'])
                    return employee
                    break
            return allcrew  # samt bara 1

    def load_pilot_or_cabincrew(self, p_or_c_input):
        all_p_or_c = []
        with open('./data_files/CrewFile.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row['role'] == p_or_c_input):
                    employee = Crew(row['ssn'], row['name'], row['role'], row['rank'],
                                    row['crewlicense'], row['address'], row['phonenumber'], row['email'])
                    all_p_or_c.append(employee)
        return all_p_or_c

    def write_in_file(self, new_crew_member=''):
        f = open("/data_files/CrewFile.csv", "a")
        f.write(new_crew_member)
        f.close()

    def overwrite_crew_file(self, all_employees_list):
        f = open("./data_files/CrewFile.csv", "w")
        for line in all_employees_list:
            str_line = ','.join(line)
            a_line = str_line + "\n"
            f.write(a_line)
        f.close()
