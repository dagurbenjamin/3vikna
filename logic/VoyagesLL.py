from IOLAYER.IOAPI import IOAPI


class VoyagesLL():
    def __init__(self, a_str):
        self.a_str = a_str

    def create_voyage(self, new_voyage_list):
        # id number, date, time, staff status
        new_voyage_list = ','.join(new_voyage_list)
        return new_voyage_list

    def get_all_voyages_dict(self):
        title = 'id number, date, time, staff status'
        all_voyages_dict = {}
        title_to_list = title.split(',')
        voyagesInfo = IOAPI().load_voyages_from_file()
        for line in voyagesInfo:
            taka_newline = line.strip('\n')
            line_to_list = taka_newline.split(',')
            Id = line_to_list[0]
            dict1 = dict(zip(title_to_list, line_to_list[1:]))
            all_voyages_dict[Id] = dict1
        return all_voyages_dict

    def get_voyage(self):
        # title = "id number, date, time, staff status"?
        

    def update_voyage(self, updatedVoyage):
        IOAPI().store_voyage_to_file(updatedVoyage)
