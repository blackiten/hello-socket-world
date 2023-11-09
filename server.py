import socket

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Получение имени хоста и порта
host = socket.gethostname()
port = 8888

# Привязка к заданному порту
server_socket.bind((host, port))

# Ожидание входящих подключений
server_socket.listen(5)

print(f"Сервер готов к приему подключений на порту {port}...")

while True:
    # Устанавливаем соединение с клиентом
    client_socket, addr = server_socket.accept()

    print(f"Получено соединение с {addr}")

    while True:
        # Чтение данных от клиента
        data = client_socket.recv(1024)
        if not data:
            break

        print(f"Получено сообщение: {data.decode()}")

        # Отправка данных обратно клиенту
        client_socket.send(data)

    # Закрытие соединения с клиентом
    client_socket.close()
