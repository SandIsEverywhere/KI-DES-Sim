import socket
import DES

def handle_client_connection(client_socket, addr):
    print(f"Got a connection from {addr}")
    
    message = client_socket.recv(1024)
    print(f"Received encrypted message: {message.decode()}")

    rkb_rev = DES.rkb[::-1]
    rk_rev = DES.rk[::-1]
    decrypted_message = DES.encrypt(message.decode(), rkb_rev, rk_rev)

    print(f"Decrypted message: {decrypted_message}")
    
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = '0.0.0.0'
    port = 65432

    server_socket.bind((host, port))

    server_socket.listen(1)
    # print(f"Listening on {host}:{port} ...")
    
    try:
        while True:
            client_socket, addr = server_socket.accept()

            handle_client_connection(client_socket, addr)
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

start_server()