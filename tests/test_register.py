import unittest
from app.models.register import Register


class TestRegistration(unittest.TestCase):
    def setUp(self):
         self.register = Register()
         user = User('test', 'test@mail.com', 'password1')
        return user

    def test_add_user(self):
        self.assertEqual(self.add_user())
          # Tests that a user has been created
        self.assertNotEqual(len(users), 0)
       

    def test_class_instance(self):
        # Tests whether an object is an instance of the class
 