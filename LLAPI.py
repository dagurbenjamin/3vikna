from DataLayer import IOAPI
title = 'ssn,name,role,rank,licence,address,phonenumber'


class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def get_all_employees(self):
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


def main():
    foo = LLAPI().get_all_employees()
    print(foo)


main()
