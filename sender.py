import socket
import DES

def client_program():
    host = '0.0.0.0'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    client_socket.send(b'Hello, Server!')

    client_socket.close()