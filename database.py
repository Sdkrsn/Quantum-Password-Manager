import sqlite3
from crypto import QuantumCrypto

class PasswordDB:
    def __init__(self, db_path='passwords.db'):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password_hash TEXT,
                public_key BLOB,
                private_key BLOB
            )
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY,
                username TEXT,
                service TEXT,
                encrypted_password BLOB,
                FOREIGN KEY(username) REFERENCES users(username)
            )
        ''')
        self.conn.commit()

    def register_user(self, username, password):
        """Register new user with quantum-safe keys"""
        phash = QuantumCrypto.hash_master_password(password)
        pubkey, privkey = QuantumCrypto.generate_kyber_keys()
        
        self.conn.execute(
            'INSERT INTO users VALUES (?,?,?,?)',
            (username, phash, pubkey, privkey)
        )
        self.conn.commit()

    # Add other methods like get_password, store_password, etc.