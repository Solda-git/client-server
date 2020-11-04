import json
import logging
import sys
from socket import socket, AF_INET, SOCK_STREAM
from time import time

from lib.routines import send_message, get_message
from lib.settings import ONLINE, COMMAND, TIMESTAMP, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP_ADDRESS, \
    DEFAULT_PORT

import log.config.client_log_config

C_LOGGER = logging.getLogger('each.client.log')

def make_online(account='guest'):
    """
    function generates request making chat user online

    :param account:
    :return:
    """
    online_msg = {
        COMMAND: ONLINE,
        TIMESTAMP: time(),
        USER: {
            ACCOUNT_NAME: account
        }
    }
    C_LOGGER.debug(f'Online message for user {online_msg[USER][ACCOUNT_NAME]} created: {online_msg}.')
    return online_msg


def parse_server_answer(message):
    """
    function processes message from the server
    :param message:
    :return: dict with status
    """
    C_LOGGER.debug(f'Parsing server message: {message}.')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return f'Correct message with response {message[RESPONSE]}.'
        return f'Bad response. {message[RESPONSE]}: {message[ERROR]}'
    raise ValueError

def main():
    """
      main function. Loading params from the command line:
            <port>, <address>
      :return:
      """

    try:
        each_server_port = int(sys.argv[1])
        each_server_address = sys.argv[2]
        if each_server_port <= 1024 and each_server_port > 65535:
            print(each_server_port)
            raise ValueError
    except IndexError:
        each_server_address = DEFAULT_IP_ADDRESS
        each_server_port = DEFAULT_PORT
        C_LOGGER.info(f'Port and address assigned to the default values.')
    except ValueError:
        C_LOGGER.critical(f"Bad port number entered: {each_server_port} (must lay between 1024 and 65536).")
        sys.exit(1)

    C_LOGGER.info(f'Port: {each_server_port} and  address: {each_server_address} - assigned.')
    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((each_server_address, each_server_port))
        C_LOGGER.info('Client connected to server.')
        online_msg =  make_online()
        send_message(client_socket, online_msg)
        C_LOGGER.info(f'Message: {online_msg} sent to server.')
        response_message = parse_server_answer(get_message(client_socket))
        C_LOGGER.info(f'Received message from the server: {response_message}.')
    except (ValueError, json.JSONDecodeError):
        C_LOGGER.error("Incorrect client message received. Can\'t decode server message.")
    except ConnectionRefusedError:
        C_LOGGER.critical(f'Can\'t connect to server.')

if __name__ == '__main__':
    main()
