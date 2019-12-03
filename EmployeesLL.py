from DataLayer import IOAPI
employee_number = 1


class EmployeesLL():
    def __init__(self, new_empl_list, employee_number):
        self.new_empl_list = new_empl_list
        self.employee_number = employee_number

    def create_ID(self, new_empl_list):
        number = self.employee_number
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
                                          first_name, last_name, employee_number)
        self.employee_number += 1
        new_empl_list.append(employee_id)
        employee_str = ", ".join(new_empl_list)
        return employee_str

    def get_all_employees():
        x = IOAPI()
        foo = x.load_crew_from_file()
        print(foo)

    def get_employee():
        pass

    def update_employee():
        pass


#ssn,name,role,rank,licence,address,phonenumber, email
a_list = ['2910858778', 'Virginia Ho', 'Pilot', 'Captain',
          'NABAE146', 'Fellsmuli 2', '8998802', 'virginia@NaN.is']

a = EmployeesLL(a_list, employee_number)
a.create_ID(a_list)


b_list = ['2209955782', 'Allen Ley', 'Pilot', 'Copilot',
          'NABAE146', 'Fellsmuli 4', '8998804', 'allen@NaN.is']
b = EmployeesLL(b_list, employee_number)
b.create_ID(b_list)

c_list = ['409858797', 'Evelyn Pickhardt', 'Cabincrew',
          'Flight Service Manager', 'N/A', 'Fellsmuli 20', '8998820', 'evelyn@NaN.is']
c = EmployeesLL(c_list, employee_number)
c.create_ID(c_list)

d_list = ['1103647756', 'Wilma Horne', 'Cabincrew',
          'Flight Attendant', 'N/A', 'Fellsmuli 25', '8998825', 'Wilma@NaN.is']
d = EmployeesLL(d_list, employee_number)
d.create_ID(d_list)

f = EmployeesLL()
f.get_all_employees()
