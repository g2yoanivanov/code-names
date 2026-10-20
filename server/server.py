import socket

from settings import network_config


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((network_config.HOST, network_config.PORT))
    server.listen()

    print(f'Listening on port {network_config.PORT}...')

    conn, addr = server.accept()
    print('Connected by {addr}')

    while True:
        data = conn.recv(1024)
        if not data:
            break

        print("Received:", data.decode())
        conn.sendall(b"Message received")

    conn.close()
