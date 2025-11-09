import unittest
from core.password_manager import PasswordManager

class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        self.manager = PasswordManager()

    def test_generate_valid_password(self):
        password = self.manager.generate_password(12)
        self.assertEqual(len(password), 12)

    def test_generate_short_password(self):
        password = self.manager.generate_password(4)
        self.assertTrue(password.startswith("[Error]"))

if __name__ == "__main__":
    unittest.main()
