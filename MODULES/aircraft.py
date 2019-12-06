class Aircraft:

    def __init__(self, insignia, typeid):
        self.insignia = insignia
        self.typeid = typeid
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{},{}".format(self.insignia, self.typeid)

    def get_insignia(self):
        return self.insignia
    
    def get_typeid(self):
        return self.get_typeid

    def set_insignia(self, new):
        self.insignia = new
    
    def set_typeid(self, new):
        self.typeid = new