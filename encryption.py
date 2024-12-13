# encryption.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Генерация случайного симметричного ключа для AES (256 бит)
def generate_aes_key():
    return os.urandom(32)  # 256 бит

# Шифрование файла с использованием AES
def encrypt_file(file_path, key):
    iv = os.urandom(16)  # Генерация случайного IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        file_data = f.read()
        # Дополнение данных до кратности 16 (размер блока AES)
        padding_length = 16 - (len(file_data) % 16)
        file_data += bytes([padding_length]) * padding_length
        
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()

    with open(f'{file_path}.enc', 'wb') as f:
        f.write(iv + encrypted_data)

    return f'{file_path}.enc'

# Дешифровка файла с использованием AES
def decrypt_file(encrypted_path, key):
    with open(encrypted_path, 'rb') as f:
        iv = f.read(16)  # Извлечение IV из начала файла
        encrypted_data = f.read()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    padding_length = decrypted_data[-1]
    return decrypted_data[:-padding_length]