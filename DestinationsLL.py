from LLAPI import LLAPI

class DestinationsLL():
    
    def __init__(self,new_dest_list=[]):
        self.new_dest_list = new_dest_list

    def create_destination(self, new_destination_list):
        #id,destination,country,distance,contactname,emergencynumber,flighttime,destinationnumber
        new_destination_list = ','.join(new_destination_list)
        return new_destination_list

    def get_destinations(self):
        a = LLAPI()
        all_destinations = a.get_all_destinations()
        return all_destinations
        
    def get_destinationinfo(self):
        pass

