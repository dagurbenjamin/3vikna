class Crew:

    def __init__(self, social, name, role, rank, user_license, address, phone, email, user_id):
        self.social = social
        self.name = name
        self.role = role
        self.rank = rank
        self.user_license = user_license
        self.address = address
        self.phone = phone
        self.email = email
        self.user_id = user_idx

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.social, self.name, self.role, self.rank, self.user_license,
                                                   self.address, self.phone, self.email, self.user_id)

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
        return self.user_licence

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_id(self):
        return self.user_id
