import socket
import DES

def client_program():
    host = '127.0.0.1'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    # client_socket.send(b'Hello, Server!')

    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        rkb = DES.rkb
        rk = DES.rk
        padded_message = message + (8 - len(message) % 8) * ' '  # Pad message to be multiple of 8
        encrypted_message = DES.encrypt(DES.strToHex(padded_message), rkb, rk)

        print(f"Sending encrypted message: {DES.binToStr(encrypted_message)}")
        client_socket.send(encrypted_message.encode())

    client_socket.close()

client_program()