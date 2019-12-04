# ssn,name,role,rank,licence,address,phonenumber
# 3009907461,William Carillo,Pilot,Captain,NAFokkerF100,Fellsmúli 1,8998801
from DataLayer import IOAPI
title = 'ssn,name,role,rank,licence,address,phonenumber'


class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def getEmployee(self):
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


foo = LLAPI().getEmployee()
print(foo)
