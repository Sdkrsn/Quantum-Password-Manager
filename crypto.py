from argon2 import PasswordHasher
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

ph = PasswordHasher()

def hash_master_password(password):
    return ph.hash(password)

def verify_master_password(hashed, password):
    try:
        ph.verify(hashed, password)
        return True
    except Exception:
        return False

def encrypt_password(key, password):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(password.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt_password(key, encrypted):
    data = base64.b64decode(encrypted)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

# You can later add Kyber key exchange logic here using e.g., pyCRYSTALS or simulate it
