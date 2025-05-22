from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_log(log_data, key):
    cipher = Fernet(key)
    return cipher.encrypt(log_data.encode())