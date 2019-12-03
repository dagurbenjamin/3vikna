from DataLayer import IOAPI


class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def get_all_employees(self):
        employee_list = []
        j = IOAPI()
        employeesInfo = j.load_crew_from_file()
        for line in employeesInfo:
            inner_list = []
            inner_list.append(line)
            employee_list.append(inner_list)
        # todo splitta innerlist
        print('LLAPI get_all_employes')
        return employee_list


def main():
    a = LLAPI()
    foo = a.get_all_employees()
    # print(foo)


main()
