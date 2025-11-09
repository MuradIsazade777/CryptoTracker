import unittest
import os
from core.wallet_store import WalletStore

class TestWalletStore(unittest.TestCase):
    def setUp(self):
        self.store = WalletStore()
        self.test_file = self.store.storage_path
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_wallet(self):
        self.store.save_wallet("TestWallet", "PrivateKey123")
        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file, "r") as file:
            content = file.read()
            self.assertIn("TestWallet", content)

if __name__ == "__main__":
    unittest.main()
