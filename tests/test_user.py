import unittest
from app.models.user_model import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('maria@gmail.com', 'maria', 'mia', '124564')

    def teardown(self):
        del self.user

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)
    
    def test_create_user(self):
        self.assertEqual(self.user.email, "maria@gmail.com")
        self.assertEqual(self.user.firstname, "maria")
        self.assertEqual(self.user.lastname, "mia")
        self.assertEqual(self.user.password, "124564")

    def test_validate_email(self):
        self.assertIsInstance(self.user.email, str)
         
    def test_validate_firstname(self):
        self.assertIsInstance(self.user.firstname, str)
    
    def test_validate_lastname(self):
        self.assertIsInstance(self.user.lastname, str)
