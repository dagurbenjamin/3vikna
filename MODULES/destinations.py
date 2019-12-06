class Destinations():

    def __init__(self, id, destination, country, distance, contactname, emergencynumber, flighttime, destinationnumber):
        self.id = id
        self.destination = destination
        self.country = country
        self.distance = distance
        self.contactname = contactname
        self.emergencynumber = emergencynumber
        self.flighttime = flighttime
        self.destinationnumber = destinationnumber

    def get_id(self):
        return self.id
    
    def get_destination(self):
        return self.destination

    def get_country(self):
        return self.country

    def get_distance(self):
        return self.distance

    def get_contactname(self):
        return self.contactname

    def get_emergencynumber(self):
        return self.emergencynumber

    def get_flighttime(self):
        return self.flighttime

    def get_destinationnumber(self):
        return self.destinationnumber

    def set_id(self, new):
        self.id = new

    def set_destination(self, new):
        self.destination = new

    def set_country(self, new):
        self.country = new

    def set_distance(self, new):
        self.distance = new

    def set_contactname(self, new):
        self.contactname = new

    def set_emergencynumber(self, new):
        self.emergencynumber = new

    def set_flighttime(self, new):
        self.flighttime = new

    def set_destinationnumber(self, new):
        self.destinationnumber = new    

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.id, self.destination, self.country, self.distance,
                                                   self.contactname, self.emergencynumber, self.flighttime, self.destinationnumber)

    