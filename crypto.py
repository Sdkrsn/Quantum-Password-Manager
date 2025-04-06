from pqcrypto.kem import kyber512
from argon2 import PasswordHasher
import os

class QuantumCrypto:
    @staticmethod
    def generate_kyber_keys():
        """Generate quantum-safe key pair"""
        return kyber512.keypair()

    @staticmethod
    def encrypt_password(password, public_key):
        """Encrypt password using Kyber"""
        ciphertext, _ = kyber512.enc(public_key)
        return ciphertext

    @staticmethod
    def hash_master_password(password):
        """Hash password with Argon2"""
        ph = PasswordHasher(
            time_cost=3,       # Increased from default 2
            memory_cost=65536, # 64MB memory usage
            parallelism=4      # Use 4 threads
        )
        return ph.hash(password)