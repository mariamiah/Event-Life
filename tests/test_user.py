import unittest
from app.models.user_model import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('maria@gmail.com', 'maria','mimi', '124')

    def teardown(self):
        del self.user
    
    def test_add_user(self):
        self.assertFalse(self.user.add_user(None, None, None, None), "Element cannot be blank")

    def test_user_class(self):
        self.assertIsInstance(self.user, User)

    def test_validate_email(self):
        self.assertIsInstance(self.user.validate_email(), str)
        self.assertEqual(self.user.validate_email(), "maria@gmail.com")
    
    def test_validate_password(self):
        self.assertEqual(self.user.password, '124')
        self.assertIsInstance(self.user.validate_password(), str)
    
    def test_valid_firstname(self):
        self.assertEqual(self.user.firstname, 'maria')
        self.assertIsInstance(self.user.email, str)
    
    def test_valid_lastname(self):
        self.assertEqual(self.user.lastname, 'mimi')
        self.assertIsInstance(self.user.email, str)
