class Voyages():
    def __init__(self, a_str):
        self.a_str = a_str

    def create_voyage():
        pass

    def get_all_voyages(self):
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

    def get_voyage():
        pass

    def update_voyage():
        pass
