special_chars = ['#', '$', '%', '^', '&', '*', '(', ')', ';']


class User:
    """ Class that registers a new user """
    def __init__(self, email, firstname, lastname, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.registered_user = dict()
    
    def add_user(self, email, firstname, lastname, password):
        if self.email is None:
            return "Email cannot be blank"
        
        if self.firstname is None:
            return "Firstname cannot be blank"

        if self.lastname is None:
            return "Lastname cannot be blank"
        
        if self.password is None:
            return "Password cannot be blank"

    def validate_email(self):
        for letter in self.email:
            if letter in special_chars:
                return "Enter valid email"
            return self.email

        if not isinstance(self.email, str):
            return 'email should be a string'
        
        if self.email is None:
            return "Element cannot be blank"

    def validate_password(self):
        if len(self.password) < 5:
            return "Password too short"
        return self.password

        if self.password is None:
            return "Element cannot be blank"
        
        if not isinstance(self.email, str):
            return 'email should be a string'

 