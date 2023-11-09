import socket

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Получение имени хоста и порта сервера
host = socket.gethostname()
port = 8888

# Подключение к серверу
client_socket.connect((host, port))

while True:
    # Ввод сообщения с консоли
    message = input("Введите сообщение для отправки на сервер (для выхода введите 'exit'): ")

    # Отправка данных на сервер
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

    # Получение данных от сервера
    data = client_socket.recv(1024)
    print(f"Получен ответ от сервера: {data.decode()}")

# Закрытие соединения
client_socket.close()
