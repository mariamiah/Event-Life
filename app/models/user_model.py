users = []
special_chars = ['#', '$', "%", '^', '&', '*', '(', ')']


class User:
    def __init__(self, email, firstname, lastname, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    def create_user(self):
        if self.email not in users:
            user = {
                
                    'email': self.email,
                    'firstname': self.firstname,
                    'lastname': self.lastname,
                    'password': self.password
                    }
            users.append(user)
            return users

    def validate_email(self):
        for letter in self.email:
            if letter in special_chars:
                print("Email invalid")
        
    def validate_firstname(self):
        for letter in self.firstname:
            if letter in special_chars:
                return "Firstname contains special characters"
    
    def validate_lastname(self):
        for letter in self.lastname:
            if letter in special_chars:
                return "lastname contains special characters"
    
    def validate_password(self):
        if len(self.password) < 5:
            return "Password is too short"       
