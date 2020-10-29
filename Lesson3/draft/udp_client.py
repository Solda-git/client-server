from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

try:
    message = 'Request from client'
    client_socket.sendto(message.encode('utf-8'), ('localhost', 8888))
    server_message, address = client_socket.recvfrom(128)
    print(server_message.decode('utf-8'))

finally:
    client_socket.close()