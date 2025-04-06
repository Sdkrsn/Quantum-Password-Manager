from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from argon2 import PasswordHasher
import os

# Simulated Kyber Key Exchange
def kyber_key_exchange():
    return os.urandom(32)  # 256-bit symmetric key

# AES Encryption
def encrypt_password(password, key):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, password.encode(), None)
    return nonce + ciphertext

def decrypt_password(encrypted_data, key):
    aesgcm = AESGCM(key)
    nonce = encrypted_data[:12]
    ct = encrypted_data[12:]
    return aesgcm.decrypt(nonce, ct, None).decode()

# Argon2 Hashing
ph = PasswordHasher()

def hash_master_password(password):
    return ph.hash(password)

def verify_master_password(hash, password):
    try:
        return ph.verify(hash, password)
    except:
        return False
