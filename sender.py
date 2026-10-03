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
        # padded_message = message + (8 - len(message) % 8) * ' '  # Pad message to be multiple of 8
        encrypted_message = DES.encrypt(DES.strToHex(message), rkb, rk)
        encrypted_hex = DES.binToHex(encrypted_message)

        print(f"Sending encrypted message: {encrypted_hex}")
        client_socket.sendall(encrypted_hex.encode("ascii"))

    client_socket.close()

client_program()