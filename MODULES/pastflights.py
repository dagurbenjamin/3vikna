

def __init__(self, departingFrom, arrivingAt, departure, arrival, aircraftID, captain, copilots, fsm, fa1, fa2):
    self.departingFrom = departingFrom
    self.arrivingAt = arrivingAt
    self.departure = departure
    self.arrival = arrival
    self.aircraftID = aircraftID
    self.captain = captain
    self.copilot = copilot
    self.fsm = fsm
    self.fa1 = fa1
    self.fa2 = fa2

def __str__(self):
    return "{},{},{},{},{},{},{},{},{},{}".format(self.departingFrom, self.arrivingAt, self.departure, self.arrival, self.aircraftID, self.captain, self.copilots, self.fsm, self.fa1, self.fa2)

def get_departingFrom(self):
    return self.departingFrom

def get_arrivingAt(self):
    return self.arrivingAt

def get_departure(self):
    return self.departure

def get_arrival(self):
    return self.arrival

def get_aircraftID(self):
    return self.aircraftID

def  get_captain(self):
    return self.captain

def get_copilot(self):
    return self.copilot

def get_fsm(self):
    return self.fsm

def get_fa1(self):
    return self.fa1

def get_fa2(self):
    return self.fa2
