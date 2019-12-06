class Destinations:

    def __init__(self, Id, destination):
        self.Id = Id
        self.destination = destination

    def __Str__(self):
        return "{},{}".format(self.Id, self.destination)
    
    def get_Id(self):
        return self.Id
    
    def get_destination(self):
        return self.destination

    
    