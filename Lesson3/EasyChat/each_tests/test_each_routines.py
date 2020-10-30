import json
import subprocess
from socket import socket, AF_INET, SOCK_STREAM
from unittest import TestCase, main

from each_tests.test_each_server import INCORRECT_RESPONSE_400, \
    CORRECT_RESPONSE_200, CORRECT_MESSAGE
from lib.routines import send_message

from lib.settings import DEFAULT_IP_ADDRESS, MAX_CONNECTIONS, DEFAULT_PORT, ENCODING

class TestEachServer(TestCase):

    def setUp(self):
        print('Test running...')
        print('Starting test server')
        self.process = subprocess.Popen('python run_test_server.py', shell=True)

    def tearDown(self):
        print('Shutting down test server')
        self.process.kill()

    def test_send_message(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        encoded = json.dumps(CORRECT_RESPONSE_200).encode(ENCODING)
        self.assertEqual(encoded, send_message(client_socket, CORRECT_MESSAGE))

    #
    # def test_get_message(self):
    #     pass

if __name__ == '__main__':
    print('Testing started')
    main()
