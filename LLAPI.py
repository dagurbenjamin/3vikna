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



def main():
    foo = LLAPI().get_airplane_types()
    print(foo)


main()
