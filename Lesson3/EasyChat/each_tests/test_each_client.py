""""
module contains tests for EasyChat client functions
"""
import os
import sys
from time import time
from unittest import TestCase, main
sys.path.append(os.path.join(os.getcwd(), '..'))
from each_client import make_online, parse_server_answer
from lib.settings import RESPONSE, ERROR, ONLINE, COMMAND, TIMESTAMP, USER, ACCOUNT_NAME

ONLINE_MESSAGE = {
    COMMAND: ONLINE,
    TIMESTAMP: '',
    USER: {
        ACCOUNT_NAME: 'guest'
    }
}

ONLINE_USER_MESSAGE = {
    COMMAND: ONLINE,
    TIMESTAMP: '',
    USER: {
        ACCOUNT_NAME: 'test_user'
    }
}

CORRECT_SERVER_RESPONSE = {
    RESPONSE: 200
}

ERROR_SERVER_RESPONSE = {
    RESPONSE: 400,
    ERROR: 'Bad request'
}


class TestEachClient(TestCase):
    """
       Test class with testing of EachChat server functions
       """

    def test_make_online(self):
        """
        testing of function make_online with correct argument
        :return:
        """
        result = make_online()
        result[TIMESTAMP] = ONLINE_MESSAGE[TIMESTAMP] = time()
        self.assertEqual(
            result,
            ONLINE_MESSAGE
        )

    def test_make_online_user(self):
        """
        testing of function make_online with correct argument
        :return:
        """
        user = ONLINE_USER_MESSAGE[USER][ACCOUNT_NAME] = 'test_user'
        result = make_online(user)
        result[TIMESTAMP] = ONLINE_USER_MESSAGE[TIMESTAMP] = time()
        self.assertEqual(
            result,
            ONLINE_USER_MESSAGE
        )
    def test_parse_correct_response(self):
        """
        testing of function parse_server_answer with correct server response
        :return:
        """
        self.assertEqual(
            parse_server_answer(CORRECT_SERVER_RESPONSE),
            f'Correct message with response {CORRECT_SERVER_RESPONSE[RESPONSE]}.'
        )

# на этом тесте выловил ошибку скобок {} !
    def test_parse_error_response(self):
        """
        testing of function parse_server_answer with bad server response
        :return:
        """
        self.assertEqual(
            parse_server_answer(ERROR_SERVER_RESPONSE),
            f'Bad response. {ERROR_SERVER_RESPONSE[RESPONSE]}: {ERROR_SERVER_RESPONSE[ERROR]}'
        )

    def test_no_response(self):
        """
        testing of function parse_server_answer with bad server response
        :return:
        """
        self.assertRaises(ValueError, parse_server_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    print('Testing started')
    main()
