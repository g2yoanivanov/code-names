import socket
from settings import network_config


def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((network_config.SERVER_IP, network_config.PORT))

    client.sendall(b"Hello server")

    response = client.recv(1024)
    print(response.decode())

    client.close()