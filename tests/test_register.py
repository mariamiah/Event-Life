import unittest
from app.models.register import Register


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.register = Register()

    def test_add_user(self):
        pass
