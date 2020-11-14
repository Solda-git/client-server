"""
Module implements basic functionality of EasyChat server

"""
import argparse
import json
import logging
import select
import sys
from datetime import time
from socket import SOCK_STREAM, AF_INET, socket

from lib.routines import get_message, send_message
from lib.settings import MAX_CONNECTIONS, COMMAND, TIMESTAMP, USER, ACCOUNT_NAME, \
    ONLINE, DEFAULT_PORT, DEFAULT_IP_ADDRESS, RESPONSE, ERROR, MESSAGE_TEXT, MESSAGE, SENDER

import log.config.server_log_config

from log.deco import log, Log

S_LOGGER = logging.getLogger('each.server.log')

@log
def parse_message(message, messages, each_client):
    """
    function parses incoming message and processes it.

    :param message: client message to be sent
    :param messages: list of messages to be sent
    :param each_client: recipient of the response message
    :return: dict with response code
    """
    S_LOGGER.debug(f'Parsing message: {message}')
    if COMMAND in message and message[COMMAND] == ONLINE and TIMESTAMP in message \
            and USER in message and ACCOUNT_NAME in message[USER] \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        send_message(each_client,
                      {
                         RESPONSE: 200
                      }
                     )

    elif COMMAND in message and message[COMMAND] == MESSAGE and TIMESTAMP in message \
            and MESSAGE_TEXT in MESSAGE:
        messages.append((message[ACCOUNT_NAME], message[MESSAGE_TEXT]))
        return

    else:
        S_LOGGER.error('Incorrect message {message}. Bad request.')
        return {
            RESPONSE: 400,
            ERROR: 'Bad request'
        }
        return

@log
def parse_args():
    """
     function parses incoming parameters of client program
     Loading params from the command line:
        -p - port
        -a - address
      :return:  server address, server port number
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.a
    server_port = namespace.p

    if not 1023 < server_port < 65536:
        S_LOGGER.critical(
            f'Invalid port assigment:'
            f'{server_port}. Available port numbers:  [1024, 65535].')
        sys.exit(1)

    return server_address, server_port



def main():
    """
    main function. Loading params from the command line:
        -p - port
        -a - address

    """
    server_address, server_port = parse_args()

    S_LOGGER.info(f'Starting server on ip-address: {server_address}, port: {server_port}')
    each_socket = socket(AF_INET, SOCK_STREAM)
    each_socket.bind((server_address, server_port))
    each_socket.settimeout(1)

    each_clients = []
    messages = []
    each_socket.listen(MAX_CONNECTIONS)
    while True:
        try:
            each_client_socket, each_client_address = each_socket.accept()
            S_LOGGER.info(f'Connection established. Client details: {each_client_address}.')
        except OSError as os_error:
            S_LOGGER.error(f'System error occurred: {os_error}')
        else:
            S_LOGGER.info(f'Connection with the client host {each_client_address} established')
            each_clients.append(each_client_socket)

        receiver_list = []
        sender_list = []
        err_list = []

        try:
            if each_clients:
                receiver_list, sender_list, err_list = select.select(each_clients, each_clients, [], 0)
        except OSError as os_error:
            S_LOGGER.error(f'System error occurred: {os_error}')

        if receiver_list:
            for sender in receiver_list:
                try:
                    parse_message(
                        get_message(sender),
                        messages,
                        sender
                    )
                except:
                    S_LOGGER.info(f'Client {sender.getpeername()} has disconnected.')
                    each_clients.remove(sender)

        if messages and sender_list:
            message = {
                COMMAND: MESSAGE,
                SENDER: messages[0][0],
                TIMESTAMP: time.time(),
                MESSAGE_TEXT: messages[0][1]
            }
            del messages[0]
            for awaiter in sender_list:
                try:
                    send_message(awaiter, message)
                except:
                    S_LOGGER.info(f'Клиент {awaiter.getpeername()} отключился от сервера.')
                    each_clients.remove(awaiter)


if __name__ == '__main__':
    main()
