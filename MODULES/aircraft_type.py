

class Aircraft_type:

    def __init__(self, type_id, manufacturer, model, capacity, empty_weight, max_takeoff_weight, unit_thrust, service_ceiling, length, height, wingspan):
        self.type_id = type_id
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.empty_weight = empty_weight
        self.max_takeoff_weight = max_takeoff_weight
        self.unit_thrust = unit_thrust
        self.service_ceiling = service_ceiling
        self.length = length
        self.height = height
        self.wingspan = wingspan

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}".format(self.type_id, self.manufacturer, self.model, self.capacity,
                                                         self.empty_weight, self.max_takeoff_weight, self.unit_thrust,
                                                         self.service_ceiling, self.length, self.height, self.wingspan)
    
    def __repr__(self):
        return self.__str__()

    def get_typeid(self):  
         return self.get_typeid

    def get_manufacturer(self):
        return self.manufacturer
    
    def get_model(self):
        return self.model
    
    def get_capacity(self):
        return self.capacity
    
    def get_eweight(self):
        return self.empty_weight

    def get_fweight(self):
        return self.max_takeoff_weight

    def get_thrust(self):
        return self.unit_thrust
    
    def get_ceiling(self):
        return self.service_ceiling
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height

    def get_wingspan(self):
        return self.wingspan



    



