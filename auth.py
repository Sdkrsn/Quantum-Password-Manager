from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class AuthManager:
    def __init__(self, db):
        self.db = db
        self.ph = PasswordHasher()

    def login(self, username, password):
        """Verify login credentials"""
        user = self.db.get_user(username)
        if not user:
            return False
            
        try:
            return self.ph.verify(user['password_hash'], password)
        except VerifyMismatchError:
            return False