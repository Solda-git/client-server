import time
from socket import socket, AF_INET, SOCK_STREAM

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 8888))
server_socket.listen(5)
print(server_socket)
try:
    while True:
        print("listening...")
        client_socket, client_address = server_socket.accept()
        print(f'Connection request from {client_address}')
        msg = time.ctime(time.time()) + '\n'
        client_socket.send(msg.encode('utf-8'))
        client_socket.close()
finally:
    server_socket.close()
