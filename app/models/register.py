class Register:
    def __init__(self):
        self.registered_users = dict()
        
    def add_user(self, email, firstname, lastname, password):
        if email and password not in self.registered_users.keys():
            self.registered_users[email] = email
            self.registered_users[firstname]= firstname
            self.registered_users[lastname] = lastname
            self.registered_users[password] = password
