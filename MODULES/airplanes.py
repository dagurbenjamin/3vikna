

class Aircraft_type:

    def __init__(self, typeid, manufacturer, model, capacity, eweight, fweight, thrust, ceiling, length, height, wingspan):
        self.type = typeid
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.eweight = eweight
        self.fweight = fweight
        self.thrust = thrust
        self.ceiling = ceiling
        self.length = length
        self.height = height
        self.wingspan = wingspan

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}".format(self.typeid, self.manufacturer, self.model, self.capacity
                                                        self.eweight, self.fweight, self.thrust, self.ceiling,
                                                        self.length, self.height, self.wingspan)

    def get_typeid(self):  
         return self.get_typeid

    def get_manufacturer(self):
        return self.manufacturer
    
    def get_model(self):
        return self.model
    
    def get_capacity(self):
        return self.capacity
    
    def get_eweight(self):
        return self.eweight

    def get_fweight(self):
        return self.fweight

    def get_thrust(self):
        return self.thrust
    
    def get_ceiling(self):
        return self.ceiling
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height

    def get_wingspan(self):
        return self.wingspan

    



