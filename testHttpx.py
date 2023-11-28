import httpx

# Установка прокси-сервера
proxies = {
    "http://": "http://hAfqSo:arevUg@95.164.203.84:9421/"
}

# URL для отправки запроса
url = "https://shop.tastycoffee.ru/"

# Отправка GET-запроса через прокси
response = httpx.get(url, proxies=proxies)

# Проверка статуса ответа
if response.status_code == 200:
    print("Запрос успешно выполнен!")
    print("Ответ сервера:")
    print(response.text)
else:
    print(f"Ошибка выполнения запроса: {response.status_code}")