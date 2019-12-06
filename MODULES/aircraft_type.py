

class Aircraft_type:

    def __init__(self, TypeId, manufacturer, model, capacity, emptyWeight, maxtakeoffWeight, unitThrust, serviceCeiling, length, height, wingspan):
        self.type = TypeId
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.eweight = emptyWeight
        self.fweight = maxTakeoffWeight
        self.thrust = unitThrust
        self.ceiling = serviceCeiling
        self.length = length
        self.height = height
        self.wingspan = wingspan

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}".format(self.TypeId, self.manufacturer, self.model, self.capacity
                                                        self.emptyWeight, self.maxTakeoffWeight, self.unitThrust, self.serviceCeiling,
                                                        self.length, self.height, self.wingspan)

    def get_typeid(self):  
         return self.get_TypeId

    def get_manufacturer(self):
        return self.manufacturer
    
    def get_model(self):
        return self.model
    
    def get_capacity(self):
        return self.capacity
    
    def get_eweight(self):
        return self.emptyWeight

    def get_fweight(self):
        return self.maxTakeoffWeight

    def get_thrust(self):
        return self.unitThrust
    
    def get_ceiling(self):
        return self.serviceCeiling
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height

    def get_wingspan(self):
        return self.wingspan

    



