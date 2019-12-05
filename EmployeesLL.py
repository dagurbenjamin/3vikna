from LLAPI import LLAPI
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

    def get_all_employees(self):
        a = LLAPI()
        all_employees = a.get_all_employees()
        return all_employees

    def get_employee():
        pass

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


get_cabin = EmployeesLL().get_all_cabincrew()


# #bar = EmployeesLL()
# all_employess_list = bar.get_all_employees()

# # ssn,name,role,rank,licence,address,phonenumber, email
# a_list = ['2910858778', 'Virginia Ho', 'Pilot', 'Captain',
#           'NABAE146', 'Fellsmuli 2', '8998802', 'virginia@NaN.is']
# a = EmployeesLL(a_list)
# a.create_ID(a_list)

# # þegar info um employee er komið i streng þa kalla eg i :
# # foo = LLAPI().save_new_employee("Save a new employee")


# b_list = ['2209955782', 'Allen Ley', 'Pilot', 'Copilot',
#           'NABAE146', 'Fellsmuli 4', '8998804', 'allen@NaN.is']
# b = EmployeesLL(b_list)
# b.create_ID(b_list)

# c_list = ['409858797', 'Evelyn Pickhardt', 'Cabincrew',
#           'Flight Service Manager', 'N/A', 'Fellsmuli 20', '8998820', 'evelyn@NaN.is']
# c = EmployeesLL(c_list)
# c.create_ID(c_list)

# d_list = ['1103647756', 'Wilma Horne', 'Cabincrew',
#           'Flight Attendant', 'N/A', 'Fellsmuli 25', '8998825', 'Wilma@NaN.is']
# d = EmployeesLL(d_list)
# d.create_ID(d_list)
