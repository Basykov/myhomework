import socket

PORT = 65432
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def handle_client(data, addr):
    print(f'New conn {addr}')
    print(f'{addr} {data.decode()}')
    response = "Повідомлення успішно отримано!"
    server.sendto(response.encode(), addr)

def start():
    print('Server started')
    while True:
        data, addr = server.recvfrom(1024)
        handle_client(data, addr)

start()

