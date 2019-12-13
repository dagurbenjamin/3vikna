from iolayer.IOAPI import IOAPI

class LLAPI():
    def __init__(self, a_str=''):
        self.a_str = a_str
        self.IOAPI = IOAPI()

    def load_destinations(self, destination_id):
        return IOAPI().load_destinations(destination_id)

    def store_destination_to_file(self, new_destination_list):
        return IOAPI().store_destination_to_file(new_destination_list)

    def update_destination_and_overwrite(self, update_destination):
        return IOAPI().update_destination_and_overwrite(update_destination)

    def load_airplanes_from_file(self, planeID):
        return IOAPI().load_airplanes_from_file(planeID)

    def store_airplanes_to_file(self, new_airplane):
        return IOAPI().store_airplanes_to_file(new_airplane)

    def load_airplanesinfo(self, planeTypeId):
        return IOAPI().load_airplanesinfo(planeTypeId)

    def store_airplanesinfo_to_file(self, new_airplane_type):
        return IOAPI().store_airplanesinfo_to_file(new_airplane_type)