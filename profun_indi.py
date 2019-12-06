from iolayer.IOAPI import IOAPI
#x = IOAPI().load_destination_from_file()
print('')
b = IOAPI().load_crew_from_file()
c = Crew("", "")
IOAPI().store_crew_to_file(c)
