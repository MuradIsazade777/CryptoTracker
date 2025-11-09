import random
import string

class PasswordManager:
    def generate_password(self, length: int = 12) -> str:
        if length < 6:
            return "[Error] Password too short."

        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))
