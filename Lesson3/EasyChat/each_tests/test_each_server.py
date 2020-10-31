""""
module contains tests for EachServer functions

"""
import os
import sys
from time import time
from unittest import TestCase, main
sys.path.append(os.path.join(os.getcwd(), '..'))
from each_server import parse_message
from lib.settings import RESPONSE, ERROR, COMMAND, ONLINE, TIMESTAMP, ACCOUNT_NAME, USER

CORRECT_RESPONSE_200 = {
    RESPONSE: 200
}
INCORRECT_RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: 'Bad request'
}

CORRECT_MESSAGE = {
    COMMAND: ONLINE,
    TIMESTAMP: time(),
    USER: {
        ACCOUNT_NAME: 'guest'
    }
}

NO_COMMAND_MESSAGE = {
    TIMESTAMP: time(),
    USER: {
        ACCOUNT_NAME: 'guest'
    }
}

WRONG_COMMAND_MESSAGE = {
    COMMAND: 'probe',
    TIMESTAMP: time(),
    USER: {
        ACCOUNT_NAME: 'guest'
    }
}

NO_TIMESTAMP_MESSAGE = {
    COMMAND: 'probe',
    USER: {
        ACCOUNT_NAME: 'guest'
    }
}

NO_USER_MESSAGE = {
    COMMAND: 'probe',
    TIMESTAMP: time(),
}

NO_USER_ACCOUNT_MESSAGE = {
    COMMAND: ONLINE,
    TIMESTAMP: time(),
    USER: {

    }
}

WRONG_USER_ACCOUNT_MESSAGE = {
    COMMAND: ONLINE,
    TIMESTAMP: time(),
    USER: {
        ACCOUNT_NAME: 'admin'
    }
}


class TestEachServer(TestCase):
    """
    Test class with testing of EachServer functions
    """

    def setUp(self):
        print('Test running...')

    def tearDown(self):
        print('Test finished!')

    def test_correct_message(self):
        """
        testing of function parse_message with correct argument
        :return:
        """
        self.assertEqual(
            parse_message(CORRECT_MESSAGE),
            CORRECT_RESPONSE_200
        )

    def test_no_command_message(self):
        """
        testing of function parse_message with incorrect argument
        :return:
        """
        self.assertEqual(
            parse_message(NO_COMMAND_MESSAGE),
            INCORRECT_RESPONSE_400
        )

    def test_wrong_command_message(self):
        """
        testing of function parse_message with incorrect argument
        :return:
        """
        self.assertEqual(
            parse_message(WRONG_COMMAND_MESSAGE),
            INCORRECT_RESPONSE_400
        )

    def test_no_timestamp_message(self):
        """
        testing of function parse_message with incorrect argument
        :return:
        """
        self.assertNotEqual(
            parse_message(NO_TIMESTAMP_MESSAGE),
            CORRECT_RESPONSE_200
        )

    def test_no_user_message(self):
        """
        testing of function parse_message with incorrect argument
        :return:
        """
        self.assertEqual(
            parse_message(NO_USER_MESSAGE),
            INCORRECT_RESPONSE_400
        )

# по результатам этого теста поправил входное условие тестируемой функции.
# добавил проверку: and ACCOUNT_NAME in message[USER]
    def test_no_user_account_message(self):
        """
        testing of function parse_message with incorrect argument
        :return:
        """
        self.assertEqual(
            parse_message(NO_USER_ACCOUNT_MESSAGE),
            INCORRECT_RESPONSE_400
        )

    def test_wrong_user_account_message(self):
        """
        testing of function parse_message with incorrect argument
        :return:
        """
        self.assertNotEqual(
            parse_message(WRONG_USER_ACCOUNT_MESSAGE),
            CORRECT_RESPONSE_200
        )


if __name__ == '__main__':
    print('Testing started')
    main()
