import os
from cryptography.fernet import Fernet

class WalletStore:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.storage_path = "data/wallets.txt"
        os.makedirs("data", exist_ok=True)

    def save_wallet(self, name: str, private_key: str):
        encrypted_key = self.cipher.encrypt(private_key.encode()).decode()
        with open(self.storage_path, "a") as file:
            file.write(f"{name}:{encrypted_key}\n")
