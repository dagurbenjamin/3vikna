#ssn,name,role,rank,licence,address,phonenumber
#3009907461,William Carillo,Pilot,Captain,NAFokkerF100,Fellsmúli 1,8998801
EMPLOYEE_NUMBER = 1
title = 'ssn,name,role,rank,licence,address,phonenumber,homenumber,email,id'
string2 = '3009907461,William Carillo,Pilot,Captain,NAFokkerF100,Fellsmúli 1,8998801,5557888,jonjonsson@nan.is,P-JJ-1'

def getEmployee(employee_str):
    string1_list = title.split(',')
    string2_list = string2.split(',')
    dict1 = dict(zip(string1_list, string2_list))
    return dict1
string2_list = string2.split(',')
employee1 = getEmployee(string2)

def generate_employee_id(employee_str):
    number = EMPLOYEE_NUMBER
    name_list = string2_list[1].split()
    id_number = ''
    id_number += string2_list[2][0]
    id_number += '-'
    id_number += string2_list[1][0]
    id_number += name_list[1][0]
    id_number += '-'
    id_number += str(number)
    EMPLOYEE_NUMBER += 1
    print(id_number)
    print(EMPLOYEE_NUMBER)
    return id_number
    
print(generate_employee_id(string2_list))


'''
def printEmployee(string_list):
    print('****************************************************************')
    print('                                                                ')
    print('		        NaN Air                "q" - quitAndSave           ')
    print('                                                                ')
    print('****************************************************************')
    print('                                                                ')
    print('              ---------------------------------------           ')
    print('                         Employee: P-JJ-1                       ')
    print('              ---------------------------------------           ')
    print('                                                                ')
    print('                                                                ')
    print('      Name                   Social               Address       ')
    print('    -------------          ----------           ----------')
    print('    {}         {}          {}          '.format(string_list[1],string_list[0],string_list[5]))
    print('                                                                ')
    print('                                                                ')
    print('  Phone number     Home number         Email          ID        ')
    print('  ------------     -----------        --------      ------      ')
    print('     {}        {}       {}  {}'.format(string_list[6],string_list[7],string_list[8],string_list[9]))
    print('                                                                ')
    print('                                                                ')
    print('           Role         Rank            License                 ')
    print('         -------      -------          ---------                ')
    print('         {}       {}          {}'.format(string_list[2],string_list[3],string_list[4]))
    print('                                                                ')
    print('Save Employee........."se"                                      ')
    print('Cancel................"c"                                       ')
    

    return


printEmployee(string2_list) '''


    


