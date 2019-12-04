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
        title = 'id,destination,country,distance,contactname,emergencynumber,flighttime,destinationnumber'
        all_destinations_dict = {}
        title_to_list = title.split(',')
        destinationsInfo = IOAPI().load_destination_from_file()
        for line in destinationsInfo:
            taka_newline = line.strip('\n')
            line_to_list = taka_newline.split(',')
            Id = line_to_list[0]
            dict1 = dict(zip(title_to_list, line_to_list))
            all_destinations_dict[Id] = dict1
        return all_destinations_dict

    def save_new_destination(self, newDestination):
        IOAPI().store_destination_to_file(newDestination)

    def get_airplane_types(self):
        title = 'planeTypeId,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan'
        plane_types_dict = {}
        title_to_list = title.split(',')
        airplanesInfo = IOAPI().load_airplanesinfo_from_file()
        for line in airplanesInfo:
            remove_newline = line.strip('\n')
            line_to_list = remove_newline.split(',')
            Id = line_to_list[-1]
            dict1 = dict(zip(title_to_list, line_to_list))
            plane_types_dict[Id] = dict1
        return plane_types_dict


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


def main():
    #foo = LLAPI().get_airplane_types()
    #print(foo)
    #fuu = LLAPI().get_past_flights()
    #print(fuu)
    fii = LLAPI().get_all_destinations()
    print(fii)

main()
