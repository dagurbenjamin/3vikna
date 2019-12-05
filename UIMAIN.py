from LLAPI import LLAPI

class UIMAIN():
    def __init__(self):
        pass
    def get_all_destinations(self):
        all_destinations_dict = LLAPI().get_all_destinations
        return all_destinations_dict



