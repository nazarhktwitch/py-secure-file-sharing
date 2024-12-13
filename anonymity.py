# anonymity.py
import requests
from stem import Signal
from stem.control import Controller

# Подключение к Tor
def connect_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()  # Подключение к Tor
        controller.signal(Signal.NEWNYM)  # Новый идентификатор для сессии

# Загрузка файла через Tor
def upload_file_via_tor(file_path, url):
    connect_tor()  # Подключение через Tor
    with open(file_path, 'rb') as f:
        file_data = f.read()
    response = requests.post(url, files={'file': file_data}, proxies={"http": "socks5h://localhost:9050"})
    return response.status_code