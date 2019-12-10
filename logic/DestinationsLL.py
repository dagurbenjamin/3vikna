
from iolayer.DestinationsIO import DestinationsIO


class DestinationsLL():

    def __init__(self, new_dest_list=[]):
        self.new_dest_list = new_dest_list

    def create_destination(self, new_destination_list):
        # id,destination,country,distance,contactname,emergencynumber,flighttime,destinationnumber
        new_destination_list = ','.join(new_destination_list)
        return new_destination_list

    def update_destination(self, destination_to_change_input, replacement_value, index_to_replace):
        all_destinatios = DestinationsIO().load_destination_from_file(
            destination_to_change_input)
        for destination in all_destinatios:
            str_dest = str(destination)
            list_destination = str_dest.split(',')
            list_destination[index_to_replace] = replacement_value
            DestinationsLL().change_the_big_destinations_list(
                destination_to_change_input, list_destination)

    def change_the_big_destinations_list(self, destination_to_change_input, changed_destination, input_value='0'):
        Destinations_all = DestinationsIO().load_destination_from_file(input_value)
        the_list = []
        for dest in Destinations_all:
            str_destination = str(dest)
            list_dest = str_destination.split(',')
            if list_dest[0] == destination_to_change_input:
                list_dest = changed_destination
            the_list.append(list_dest)
        header = ['id', 'destination', 'country', 'distance', 'contactname',
                  'emergencynumber', 'flighttime', 'destinationnumber']
        the_list.insert(0, header)
        DestinationsIO().overwrite_destination_file(the_list)

    def get_destination(self, destination_id):
        one_destination = DestinationsIO().load_destination_from_file(destination_id)
        return one_destination