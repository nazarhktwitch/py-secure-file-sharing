# storage.py
import ipfshttpclient

# Загрузка файла в IPFS
def upload_file_to_ipfs(file_path):
    client = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')
    result = client.add(file_path)
    return result['Hash']

# Загрузка файла по хешу из IPFS
def download_file_from_ipfs(file_hash):
    client = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')
    file_path = client.get(file_hash)  # Получаем файл по хешу
    return file_path