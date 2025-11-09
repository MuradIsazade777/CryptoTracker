import unittest
from core.crypto_engine import CryptoEngine

class TestCryptoEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CryptoEngine()

    def test_encrypt_decrypt(self):
        text = "Hello Crypto"
        encrypted = self.engine.encrypt_text(text)
        decrypted = self.engine.decrypt_text(encrypted)
        self.assertEqual(decrypted, text)

    def test_invalid_decrypt(self):
        result = self.engine.decrypt_text("invalid_data")
        self.assertTrue(result.startswith("[Error]"))

if __name__ == "__main__":
    unittest.main()
