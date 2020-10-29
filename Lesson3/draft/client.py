from socket import socket, AF_INET, SOCK_STREAM

try:
    while True:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(('localhost', 8888))
        msg = client_socket.recv(4096)
        client_socket.close()

        print(f"Server time: {msg.decode('utf-8')}")

finally:
    client_socket.close()

