import socket

PORT = 65432
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.connect(ADDR)
    message = "Повідомлення для сервера"
    client.sendto(message.encode(), ADDR)
    response, server_address = client.recvfrom(1024)
    print(f"Отримано від сервера ({server_address}): {response.decode()}")