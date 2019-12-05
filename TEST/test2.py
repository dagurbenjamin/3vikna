#ssn,name,role,rank,licence,address,phonenumber
#3009907461,William Carillo,Pilot,Captain,NAFokkerF100,Fellsmúli 1,8998801
id = "COP-CJ-1"
title = 'ssn,name,role,rank,licence,address,phonenumber'
string2 = '3009907461,William Carillo,Pilot,Captain,NAFokkerF100,Fellsmúli 1,8998801,5557888,jonjonsson@nan.is'

def getEmployee(employee_str):
    string1_list = title.split(',')
    employee_list = []
    employee_list = string2.split(',')
    all_employees_dict = {}
    dict1 = dict(zip(string1_list, employee_list))
    all_employees_dict[id] = dict1
    return all_employees_dict

    


employee1 = getEmployee(string2)
print(employee1)


