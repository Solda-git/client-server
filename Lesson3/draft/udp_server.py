from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

server_socket.bind(('', 8888))

try:
    while True:
        message, address = server_socket.recvfrom(1024)
        print(address)
        print(message.decode('utf-8'))
        answer = 'Response from udp server'
        server_socket.sendto(answer.encode('utf-8'), address)
finally:
    server_socket.close()
