from DataLayer import IOAPI


def get_all_employees(IOAPI):
        filestream_crew = IOAPI.load_crew_from_file()
        for line in filestream_crew:
            print(line)
