from iolayer.AirplanesIO import AirplanesIO
from logic.LLAPI import LLAPI


class AirplanesLL:
    def __init__(self, plane_list=''):
        self.plane_list = plane_list
        self.LLAPI = LLAPI()

    def save_new_airplane_info(self, airplaneInfo):
        LLAPI().store_airplanes_to_file(airplaneInfo)

    def save_new_airplane(self, airplane):
        LLAPI().store_airplanes_to_file(airplane)

    def get_info_about_one_airplane(self, planeTypeId):
        info_about_one_airplane = LLAPI().load_airplanesinfo(planeTypeId)
        return info_about_one_airplane

    def get_all_airplanes_info(self):
        all_airplanes_info = LLAPI().load_airplanesinfo('0')
        all_aiplanes_info_list = []
        for aiplaneinfo in all_airplanes_info:
            str_aiplaneinfo = str(aiplaneinfo)
            list_aiplaneinfo = str_aiplaneinfo.split(',')
            all_aiplanes_info_list.append(list_aiplaneinfo)
        return all_aiplanes_info_list

    def get_one_airplane(self, planeTypeId):
        get_one_airplane = LLAPI().load_airplanes_from_file(planeTypeId)
        return get_one_airplane

    def get_all_airplanes(self):
        all_airplanes = LLAPI().load_airplanes_from_file('0')
        all_airplanes_list = []
        for airplane in all_airplanes:
            str_airplane = str(airplane)
            list_airplane = str_airplane.split(',')
            all_airplanes_list.append(list_airplane)
        return all_airplanes_list

    def is_airplane_available(self, date, plane_insignia):
        all_voyages = VoyagesLL().get_voyages()
        for voyage in all_voyages:
            if voyage[1] == plane_insignia and voyage[2] == date:
                return False
        else:
            return True
    #MUNA AÐ BREYTA!!!!!!!!!!!!!!!!!!!!!