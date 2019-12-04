from LLAPI import LLAPI

class UIAPI():
    def __init__(self):
        pass
    def get_all_destinations(self):
        all_destinations_list = LLAPI().get_all_destinations
        return all_destinations_list



