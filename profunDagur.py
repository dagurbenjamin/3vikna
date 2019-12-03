class AirplanesLL:
    def __init__(self, plane_list):
        self.plane_list = plane_list


    def create_airplane_info(self, plane_list):
        plane_list = ", ".join(plane_list)
        return plane_list


    def new_airplane(self, new_plane):
        new_plane = ", ".join(new_plane)
        print(new_plane)


    def get_airplanes(self):
            


    def get_airplane_types(self):


    def update_airplane(self):
        pass

def main():
    plane_list = ["NABAE146", "BAE", "146", "82", "23820", "38101", "31.1", "11000", "26.19", "8.61", "26", "34"]
    new_plane = ["stuff", "more stuff"]
    a = AirplanesLL(plane_list)
    a.create_airplane_info(plane_list)
    b = AirplanesLL(new_plane)
    b.new_airplane(new_plane)
main()