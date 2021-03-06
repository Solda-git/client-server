"""
module containes test server socket to test Easy Chat routine functions

"""

import json
import os
import sys
from socket import socket, AF_INET, SOCK_STREAM

sys.path.append(os.path.join(os.getcwd(), '..'))
from each_server import parse_message
from lib.routines import get_message, send_message
from lib.settings import MAX_CONNECTIONS, DEFAULT_PORT

print('Running test server')
each_server_socket = socket(AF_INET, SOCK_STREAM)
each_server_socket.bind(('', DEFAULT_PORT))
each_server_socket.listen(MAX_CONNECTIONS)

while True:
    each_client_socket, each_client_address = each_server_socket.accept()
    try:
        client_message = get_message(each_client_socket)
        server_response = parse_message(client_message)
        send_message(each_client_socket, server_response)
        each_client_socket.close()
    except (ValueError, json.JSONDecodeError):
        print('Incorrect client message received.')
        each_client_socket.close()
