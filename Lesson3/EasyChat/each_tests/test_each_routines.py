import json
import os
import subprocess
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from unittest import TestCase, main

sys.path.append(os.path.join(os.getcwd(), '..'))
from each_tests.test_each_server import INCORRECT_RESPONSE_400, \
    CORRECT_RESPONSE_200, CORRECT_MESSAGE, NO_COMMAND_MESSAGE
from lib.routines import send_message, get_message

from lib.settings import DEFAULT_IP_ADDRESS, MAX_CONNECTIONS, DEFAULT_PORT, ENCODING

PROCESS = None
COUNTER = 0

class TestEachRountines1(TestCase):

    def test_send_get_message(self):
        proc = subprocess.Popen(['python3', 'run_test_server.py'])
        time.sleep(1)

        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        encoded = json.dumps(CORRECT_MESSAGE).encode(ENCODING)
        self.assertEqual(encoded, send_message(client_socket, CORRECT_MESSAGE))
        self.assertEqual(get_message(client_socket), CORRECT_RESPONSE_200)

        client_socket.close()
        proc.kill()

if __name__ == '__main__':
    print('Testing started')
    main()

