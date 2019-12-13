from IOLAYER.IOAPI import IOAPI


class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def save_new_employee(self, newEmployee):
        IOAPI().store_crew_to_file(newEmployee)

    def save_new_destination(self, newDestination):
        IOAPI().store_destination_to_file(newDestination)


# def main():
    #foo = LLAPI().get_airplane_types()
    # print(foo)
    #fuu = LLAPI().get_past_flights()
    # print(fuu)
    #fii = LLAPI().get_airplane_types()
    # print(fii)
    #fcc = LLAPI().get_upcoming_flights()
    # print(fcc)
    #fee = LLAPI().get_all_destinations()
    # print(fee)

# main()
