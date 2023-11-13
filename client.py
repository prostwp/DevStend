import requests

# Адрес сервера
server_url = 'http://172.20.10.3:8080'

try:
    # Отправляем GET-запрос к серверу
    response = requests.get(f"{server_url}/get_link", timeout=10)

    # Проверяем успешность запроса
    if response.status_code == 200:
        print(f"Ответ сервера: {response.text}")
    else:
        print(f"Ошибка при запросе к серверу. Код состояния: {response.status_code}")
except requests.exceptions.ConnectTimeout:
    print("Ошибка подключения: превышено время ожидания.")
except requests.exceptions.ConnectionError:
    print("Ошибка подключения: не удалось установить соединение.")
