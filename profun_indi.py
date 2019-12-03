class EmployeesLL():
    def __init__(self, new_empl_list):
        self.new_empl_list = new_empl_list

    def create_ID(self, new_empl_list):
        name = new_empl_list[1].split(' ')
        print(new_empl_list)


#ssn,name,role,rank,licence,address,phonenumber, email
a_list = ['2910858778', 'Virginia Ho', 'Pilot', 'Captain',
          'NABAE146', 'Fellsmuli 2', '8998802', 'virginia@NaN.is']
a = EmployeesLL(a_list)
a.create_ID(a_list)
