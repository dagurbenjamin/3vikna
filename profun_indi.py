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

    def get_all_pilots(self):
        all_employees_dict = LLAPI().get_all_employees()
        for key in all_employees_dict:
            if key[0] == 'C':
                print(key)
                all_values = all_employees_dict[key]
                get_role = all_values
                print(get_role)
            else:
                return None

        # for [role] in all_employees_dict:
        #     if

    def get_all_cabincrew(self):
        all_employees_dict = LLAPI().get_all_employees()
        for key in all_employees_dict:
            if key[0] == 'F':
                print(key)
                all_values = all_employees_dict[key]
                get_role = all_values
                print(get_role)

    def get_employee(self, employee_id):
        pass

    def update_employee(self, employee_id_input):
        employeeInfo = EmployeesLL().get_employee()
        pass


get_pilots = EmployeesLL().get_all_cabincrew()

#bar = EmployeesLL()
#all_employess_list = bar.get_all_employees()

# ssn,name,role,rank,licence,address,phonenumber, email
# a_list = ['2910858778', 'Virginia Ho', 'Pilot', 'Captain',
#           'NABAE146', 'Fellsmuli 2', '8998802', 'virginia@NaN.is']
# a = EmployeesLL(a_list)
# a.create_ID(a_list)

# þegar info um employee er komið i streng þa kalla eg i :
# foo = LLAPI().save_new_employee("Save a new employee"
