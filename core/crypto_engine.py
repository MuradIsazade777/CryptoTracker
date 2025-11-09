from cryptography.fernet import Fernet

class CryptoEngine:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_text(self, text: str) -> str:
        return self.cipher.encrypt(text.encode()).decode()

    def decrypt_text(self, encrypted_text: str) -> str:
        try:
            return self.cipher.decrypt(encrypted_text.encode()).decode()
        except Exception:
            return "[Error] Invalid encrypted text or key."
