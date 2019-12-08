from LLAPI import LLAPI
from IOLAYER.IOAPI import IOAPI
from itertools import count


class EmployeesLL():
    _ids = count(0)

    def __init__(self, new_empl_list=[]):
        self.id = next(self._ids)
        self.new_empl_list = new_empl_list

    def create_ID(self, new_empl_list):
        number = self.id
        name = new_empl_list[1].split(' ')
        first_name = name[0][0]
        last_name = name[1][0]
        rank = new_empl_list[3].split(' ')
        if len(rank) == 3:
            rank = '{}{}{}'.format(rank[0][0], rank[1][0], rank[2][0])
        elif len(rank) == 2:
            rank = '{}{}{}'.format(rank[0][0], rank[0][1], rank[1][0])
        else:
            rank = new_empl_list[3][:3]
        employee_id = '{}-{}{}-{}'.format(str(rank).upper(),
                                          first_name, last_name, number)
        new_empl_list.append(employee_id)  # setja id fremst? fyrir dict
        employee_str = ",".join(new_empl_list)
        return employee_str

    def choose_employee_to_see(self, number, names_list):
        return names_list[number]

    def update_employee(self, employee_id_input):
        # get the crew file from data layer
        pass

    def get_all_pilots(self):
        all_cabincrew_list = []
        all_employees_dict = LLAPI().get_all_employees()
        for key in all_employees_dict:
            if key[0] == 'C':
                per_employee = []
                name = all_employees_dict[key]['name']
                per_employee.append(name)
                per_employee.append(key)
                Licence = all_employees_dict[key]['licence']
                per_employee.append(Licence)
                all_cabincrew_list.append(per_employee)
        print(all_cabincrew_list)

    def get_all_cabincrew(self):
        all_cabincrew_list = []
        all_employees_dict = LLAPI().get_all_employees()
        for key in all_employees_dict:
            if key[0] == 'F':
                per_employee = []
                name = all_employees_dict[key]['name']
                per_employee.append(name)
                per_employee.append(key)
                all_cabincrew_list.append(per_employee)
        print(all_cabincrew_list)


name = 'Allen Ley'
foo = EmployeesLL().get_employee(name)
number = 1
x = EmployeesLL().choose_employee_to_see(number, foo)

print(x)
