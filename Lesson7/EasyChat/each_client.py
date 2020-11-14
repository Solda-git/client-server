"""
Module implements basic functionality of EasyChat client

"""
import argparse
import json
import logging
import sys
from socket import socket, AF_INET, SOCK_STREAM
from time import time

from lib.routines import send_message, get_message
from lib.settings import ONLINE, COMMAND, TIMESTAMP, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, MESSAGE, MESSAGE_TEXT, SENDER

import log.config.client_log_config
from log.deco import log, Log

C_LOGGER = logging.getLogger('each.client.log')

SEND_MODE = 'send'
RECV_MODE = 'recv'

@log
# @Log()
def make_online(account='Guest'):
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
    C_LOGGER.debug(f'Online message for user {online_msg[USER][ACCOUNT_NAME]} '
                   f'created: {online_msg}.')
    return online_msg

@log
# @Log()
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

@log
def parse_args():
    """"
    function parses incoming parameters of client program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, nargs='?')
    # available modes: SEND_MODE, RECV_MODE
    parser.add_argument('-m', '--mode', default=RECV_MODE, nargs='?') # recv/send
    namespace = parser.parse_args(sys.argv[1:])
    each_server_address = namespace.addr
    each_server_port = namespace.port
    each_client_mode = namespace.mode

    if not 1023 < each_server_port < 65536:
        C_LOGGER.critical(f'Incorrect port number assigned. Client\'s start failed. '
                          f'Use port number in frame: [1024, 65535]')
        sys.exit(1)

    if each_client_mode not in [RECV_MODE, SEND_MODE]:
        C_LOGGER.critical(f'Incorrect mode {each_client_mode} set. '
                          f'Available options: {RECV_MODE}, {SEND_MODE}')
        sys.exit(1)

    return each_server_address, each_server_port, each_client_mode

@log
def create_message(each_socket, account_name='Guest'):
    """
    function creates message for the client
    """
    message_text = input('Input message text or \'q\' for exit.')
    if message_text == 'q':
        each_socket.close()
        C_LOGGER.info(f'User {each_socket} closed the connection.')
        print('Connection closed. See you next time')
        exit(0)
    message = {
        COMMAND: MESSAGE,
        TIMESTAMP: time.time(),
        ACCOUNT_NAME: account_name,
        MESSAGE_TEXT: message_text
    }
    C_LOGGER.debug(f'Message {message} prepared.')
    return  message

@log
def recv_message(message):
    """
    function receives message for the client
    """
    if COMMAND in message and message[COMMAND] == MESSAGE and \
        SENDER in message and MESSAGE_TEXT in message:
        info = f'Message {message[MESSAGE_TEXT]} received from {message[SENDER]}'
        print(inf)
        C_LOGGER.info(info)
    else:
        C_LOGGER.error(f'Incorrect message {message}')

def main():
    """
    main function
    """

    each_server_address, each_server_port, each_client_mode = parse_args()
    C_LOGGER.info(f'Port: {each_server_port} and  address: {each_server_address} - assigned.')
    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((each_server_address, each_server_port))
        C_LOGGER.info('Client connected to server.')
        online_msg = make_online()
        send_message(client_socket, online_msg)
        C_LOGGER.info(f'Message: {online_msg} sent to server.')
        response_message = parse_server_answer(get_message(client_socket))
        C_LOGGER.info(f'Received message from the server: {response_message}.')
    except (ValueError, json.JSONDecodeError):
        C_LOGGER.error("Incorrect client message received. Can\'t decode server message.")
        sys.exit(1)
    except ConnectionRefusedError:
        C_LOGGER.critical(f'Can\'t connect to server.')
        sys.exit(1)
    # connection established
    else:
        if each_client_mode == SEND_MODE:
            print(f"Client is working in '{SEND_MODE}' mode")
        else:
            print(f"Client is working in '{RECV_MODE}' mode")
        while True:
            if each_client_mode == SEND_MODE:
                try:
                    send_message(client_socket, create_message(client_socket))
                except (ConnectionResetError, ConnectionError, ConnectionRefusedError):
                    C_LOGGER.error(f'Connection with server {each_server_address} lost.')
                    sys.exit(1)
            if each_client_mode == RECV_MODE:
                try:
                    recv_message(get_message(client_socket))
                except (ConnectionResetError, ConnectionError, ConnectionRefusedError):
                    C_LOGGER.error(f'Connection with server {each_server_address} lost.')
                    sys.exit(1)

if __name__ == '__main__':
    main()
