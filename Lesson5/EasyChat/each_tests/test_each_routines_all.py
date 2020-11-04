"""
Test for EasyChat routine functions: send and receive
"""

import json
import os
import sys
from copy import deepcopy
from unittest import TestCase, main

sys.path.append(os.path.join(os.getcwd(), '..'))
from each_tests.test_each_server import CORRECT_MESSAGE, \
    INCORRECT_RESPONSE_400, CORRECT_RESPONSE_200

from lib.routines import send_message, get_message
from lib.settings import ENCODING

class TestEachSocket:
    """
    Test class that helps in testing send and receive routine functions.
    emulates Socket behavior without real network activity
    """

    def __init__(self, msg):
        self.message = deepcopy(msg)
        self.encoded_message = self.received_message = None

    def send(self, msg):
        """
        function emulates socket send feature
        :param msg:
        :return:
        """
        self.encoded_message = json.dumps(self.message).encode(ENCODING)
        self.received_message = msg

    def recv(self, max_len):
        """
        function emulates socket receive feature
        :param msg:
        :return:
        """
        return json.dumps(self.message).encode(ENCODING)


class TestEachRoutines(TestCase):
    """
    Test Class which tests send and receive routine functions.
    """
    t_int_value = 111
    t_correct_message = deepcopy(CORRECT_MESSAGE)
    t_correct_response_200 = deepcopy(CORRECT_RESPONSE_200)
    t_incorrect_response_400 = deepcopy(INCORRECT_RESPONSE_400)

    def test_send_message(self):
        """
        testing send routine function.
        :return:
        """
        t_socket = TestEachSocket(self.t_correct_message)
        self.assertEqual(
            send_message(t_socket, self.t_correct_message),
            t_socket.encoded_message
        )
        with self.assertRaises(Exception):
            send_message(t_socket, t_socket)

    def test_get_message(self):
        """
       testing receive routine function.
       :return:
       """
        t_corretct_socket_200 = TestEachSocket(self.t_correct_response_200)
        t_incorretct_socket_400 = TestEachSocket(self.t_incorrect_response_400)

        self.assertEqual(
            get_message(t_corretct_socket_200),
            self.t_correct_response_200
        )
        self.assertEqual(
            get_message(t_incorretct_socket_400),
            # get_message(self.t_int_value),
            self.t_incorrect_response_400
        )
        with self.assertRaises(AttributeError):
            get_message(self.t_int_value)

if __name__ == "__main__":
    print('Testing started')
    main()
