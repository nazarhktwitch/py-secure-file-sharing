## File Encryption Guide

### Encryption

Files are encrypted using AES in CBC (Cipher Block Chaining) mode. A random key is generated for each file to be encrypted.

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_file(file_path, key):
    iv = os.urandom(16)  # Generate a random initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        file_data = f.read()
        encrypted_data = encryptor.update(file_data) + encryptor.finalize()
        
    return encrypted_data
```

### Decryption

The same key used for encryption is required to decrypt the file.

```python
def decrypt_file(file_path, key):
    iv = os.urandom(16)  # Use the same IV as for encryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    with open(file_path, 'rb') as f:
        file_data = f.read()
        decrypted_data = decryptor.update(file_data) + decryptor.finalize()
        
    return decrypted_data
```