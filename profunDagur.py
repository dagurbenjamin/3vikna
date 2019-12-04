from DataLayer import IOAPI



class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def get_all_employees(self):
        title = 'ssn,name,role,rank,licence,address,phonenumber'
        all_employees_dict = {}
        title_to_list = title.split(',')
        employeesInfo = IOAPI().load_crew_from_file()
        for line in employeesInfo:
            taka_newline = line.strip('\n')
            line_to_list = taka_newline.split(',')
            Id = line_to_list[-1]
            dict1 = dict(zip(title_to_list, line_to_list))
            all_employees_dict[Id] = dict1
        return all_employees_dict

    def save_new_employee(self, newEmployee):
        IOAPI().store_crew_to_file(newEmployee)

    def get_all_destinations(self):
        destination_list = []
        destinationInfo = IOAPI().load_destination_from_file()
        for line in destinationInfo:
            inner_list = []
            inner_list.append(line)
            destination_list.append(inner_list)
        return destination_list

    def save_new_destination(self, newDestination):
        IOAPI().store_destination_to_file(newDestination)


    def get_past_flights(self):
        title = "departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2"
        all_past_flights_dict = {}
        title_to_list = title.split(',')
        flights_info = IOAPI().load_past_flights_from_file()
        for line in flights_info:
            take_newline = line.strip('\n')
            line_to_list = take_newline.split(',')
            Id = line_to_list[0]
            dict1 = dict(zip(title_to_list, line_to_list[1:]))
            all_past_flights_dict[Id] = dict1
        return all_past_flights_dict


    def get_upcoming_flights(self):
        title = "departingFrom,arrivingAt,departure,arrival"
        all_upcoming_flights_dict = {}
        title_to_list = title.split(',')
        flights_info = IOAPI().load_upcoming_flights_from_file()
        for line in flights_info:
            take_newline = line.strip('\n')
            line_to_list = take_newline.split(',')
            Id = line_to_list[0]
            dict1 = dict(zip(title_to_list, line_to_list[1:]))
            all_upcoming_flights_dict[Id] = dict1
        return all_upcoming_flights_dict


def main():
    fuu = LLAPI().get_past_flights()
    print(fuu)
    fii = LLAPI().get_upcoming_flights()
    print(fii)

main()
