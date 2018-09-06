class Person:
    def __init__(self, name, age, color, origin, gender):
        self.name = name
        self.age = age
        self.color = color
        self.origin = origin
        self.gender = gender
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age


class User(Person):
    def __init__(self, email, firstname, lastname, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
    
    def get_email(self):
        return self.email
    
    def get_name(self):
        return self.firstname + self.lastname


class GuestList(self):
    pass
