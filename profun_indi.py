from DataLayer import IOAPI


filestream_crew = IOAPI().load_crew_from_file(a_str)
for line in filestream_crew:
    print(line)
