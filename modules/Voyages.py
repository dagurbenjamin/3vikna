class Voyages:

    def __init__(self, voyageID, planeInsignia, date, destination, captain, copilot, FlightServiceManager, flightAttendant):
        self.voyageID = voyageID
        self.planeInsignia = planeInsignia
        self.date = date
        self.destination = destination
        self.captain = captain
        self.copilot = copilot
        self.FlightServiceManager = FlightServiceManager
        self.flightAttendant = flightAttendant

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.voyageID, self.planeInsignia, self.date, self.destination, self.captain, self.copilot, self.FlightServiceManager, self.flightAttendant)

    def get_voyageID(self):
        return self.voyageID

    def get_planeInsignia(self):
        return self.planeInsignia

    def get_date(self):
        return self.date

    def get_destination(self):
        return self.destination

    def get_captain(self):
        return self.captain

    def get_copilot(self):
        return self.copilot

    def get_FlightServiceManager(self):
        return self.FlightServiceManager

    def get_flightAttendant(self):
        return self.flightAttendant

    def set_voyageID(self, new):
        self.voyageID = new

    def set_planeInsignia(self, new):
        self.planeInsignia = new

    def set_date(self, new):
        self.date = new

    def set_destination(self, new):
        self.destination = new

    def set_captain(self, new):
        self.captain = new

    def set_copilot(self, new):
        self.copilot = new

    def set_FlightServiceManager(self, new):
        self.arrivFlightServiceManageral = new

    def set_flightAttendant(self, new):
        self.flightAttendant = new
