class Crew:

    def __init__(self, social, name, role, rank, crewlicense, address, phone, email):
        self.social = social
        self.name = name
        self.role = role
        self.rank = rank
        self.crewlicense = crewlicense
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.social, self.name, self.role, self.rank, self.crewlicense,
                                                self.address, self.phone, self.email)

    def __repr__(self):
        return self.__str__()

    def get_social(self):
        return self.social

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_rank(self):
        return self.rank

    def get_license(self):
        return self.crewlicense

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def set_social(self, new):
        self.social = new

    def set_name(self, new):
        self.name = new

    def set_role(self, new):
        self.role = new

    def set_rank(self, new):
        self.rank = new

    def set_license(self, new):
        self.license = new

    def set_address(self, new):
        self.address = new

    def set_phone(self, new):
        self.phone = new

    def set_email(self, new):
        self.email = new
