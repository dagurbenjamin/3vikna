class CrewIO(IOAPI):
    def __init__(self, a_str=''):
        self.a_str = a_str

    def write_in_file(self, new_crew_member=''):
        f = open("CrewFile.csv", "a")
        f.write(new_crew_member)
        f.close()

    def overwrite_crew_file(self, updated_employees_str=''):
        f = open("CrewFile.csv", "w")
        f.write(updated_employees_str)
        f.close()
