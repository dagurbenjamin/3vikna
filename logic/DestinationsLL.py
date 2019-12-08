from LLAPI import LLAPI


class DestinationsLL():

    def __init__(self, new_dest_list=[]):
        self.new_dest_list = new_dest_list

    def create_destination(self, new_destination_list):
        # id,destination,country,distance,contactname,emergencynumber,flighttime,destinationnumber
        new_destination_list = ','.join(new_destination_list)
        return new_destination_list

    def get_all_destinations(self):
        pass

    def get_destination(self):
        pass

    def update_destination(self, destinations_id_input):
        # get the destination file from data layer
        pass
