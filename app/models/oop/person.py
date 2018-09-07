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
    def __init__(self, name, age, color, event_category):
        super().__init__(name, age, color)
        self.event_category = event_category
    
    def description(self):
        return "{} belongs to {} category".format(super().get_name(), self.event_category)


class GuestList:
    def __init__(self):
        self.registered_users = dict()
    
    def user_exists(self, name):
        return self.registered_users.__contains__(name)
    
    def add_users(self, user):
        if (self.user_exists(user.name)):
            return "User already exists"
        self.registered_users[user.name] = user

    def find_user_by_name(self, name):
        if (self.user_exists(name)):
            return self.registered_users[name]
        return "User doesnot exist"

    def delete_user(self, name):
        if (self.user_exists(name)):
            del self.registered_users[name]
        else:
            return "User does not exist"
