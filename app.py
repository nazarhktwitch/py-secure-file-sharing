import os
from encryption import encrypt_file, decrypt_file, generate_aes_key
from storage import upload_file_to_ipfs, download_file_from_ipfs
from anonymity import upload_file_via_tor
from crypto_keys import generate_keys, sign_data, verify_signature
import settings

# Получаем путь к директории, где находится сам скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Формируем полный путь к файлу, который находится в той же директории, что и скрипт
file_path = os.path.join(script_dir, 'example.txt')

# Выводим путь к файлу для отладки
print(f"Looking for file in: {file_path}")

# Генерация симметричного ключа для AES
aes_key = generate_aes_key()

# Шифрование файла
encrypted_file = encrypt_file(file_path, aes_key)  # Шифруем файл с использованием AES
print(f"Encrypted file: {encrypted_file}")

# Загрузка файла в IPFS
file_hash = upload_file_to_ipfs(encrypted_file)
print(f"File uploaded to IPFS with hash: {file_hash}")

# Получение файла из IPFS
downloaded_file_path = download_file_from_ipfs(file_hash)
print(f"File downloaded from IPFS: {downloaded_file_path}")

# Дешифровка файла
decrypted_file = decrypt_file(downloaded_file_path, aes_key)
print(f"File decrypted successfully")

# Отправка файла через Tor (если нужно)
upload_file_via_tor(decrypted_file, 'http://example.com/upload')

# Проверка подписи данных
private_key, public_key = generate_keys()
signature = sign_data(private_key, "Important data")
is_valid = verify_signature(public_key, "Important data", signature)
print(f"Signature valid: {is_valid}")