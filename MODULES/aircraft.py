class Aircraft:

    def __init__(self, insignia, typeid):
        self.insignia = insignia
        self.type.id = typeid
    
    def __str__(self):
        return "{},{}".format(self.insignia, self.typeid)

    def get_insignia(self):
        return self.insignia
    
    def get_typeid(self):
        return self.get_typeid