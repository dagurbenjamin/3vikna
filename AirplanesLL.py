from LLAPI import LLAPI

from DataLayer import IOAPI



class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str


class AirplanesLL:
    def __init__(self, plane_list):
        self.plane_list = plane_list


    def create_airplane_info(self, plane_list):
        plane_list = ",".join(plane_list)
        return plane_list


    def new_airplane(self, new_plane):
        new_plane = ",".join(new_plane)
        return new_plane


    def get_airplanes(self, the_plains):
        the_plains = list(the_plains.split(", "))
        return the_plains


    def get_airplane_types(self, plane_types):
        title = 'planeTypeId,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan'
        plane_types_dict = {}
        title_to_list = title.split(',')
        airplanesInfo = IOAPI().load_airplanesinfo_from_file()
        for line in airplanesInfo:
            remove_newline = line.strip('\n')
            line_to_list = remove_newline.split(',')
            Id = line_to_list[-1]
            dict1 = dict(zip(title_to_list, line_to_list))
            plane_types_dict[Id] = dict1
        return plane_types_dict



def main():
    plane_list = ["NABAE146", "BAE", "146", "82", "23820", "38101", "31.1", "11000", "26.19", "8.61", "26", "34"]
    new_plane = ["ID", "Name"]
    the_plains = "ID, Name"
    plain_type = "NABAE146, BAE, 146, 82, 23820, 38101, 31.1, 11000, 26.19, 8.61, 26, 34"
    a = AirplanesLL(plane_list)
    a.create_airplane_info(plane_list)
    b = AirplanesLL(new_plane)
    b.new_airplane(new_plane)
    c = AirplanesLL(the_plains)
    c.get_airplanes(the_plains)
    d = AirplanesLL(plain_type)
    d.get_airplane_types(plain_type)
main()