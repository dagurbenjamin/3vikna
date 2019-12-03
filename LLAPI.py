from DataLayer import IOAPI


class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def get_all_employees(self):
        employee_list = []
        employeesInfo = IOAPI().load_crew_from_file()
        for line in employeesInfo:
            inner_list = []
            inner_list.append(line)
            employee_list.append(inner_list)
        # todo splitta innerlist
        return employee_list

    def save_new_employee(self, newEmployee):
        IOAPI().store_crew_to_file(newEmployee)


def main():
    foo = LLAPI().get_all_employees()


main()
