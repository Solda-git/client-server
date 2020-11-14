"""
Module implements basic functionality of EasyChat server

"""

import json
import logging
import sys
from socket import SOCK_STREAM, AF_INET, socket

from lib.routines import get_message, send_message
from lib.settings import MAX_CONNECTIONS, COMMAND, TIMESTAMP, USER, ACCOUNT_NAME, \
    ONLINE, DEFAULT_PORT, DEFAULT_IP_ADDRESS, RESPONSE, ERROR

import log.config.server_log_config

from log.deco import log, Log

S_LOGGER = logging.getLogger('each.server.log')
@Log()
@log
def parse_message(message):
    """
    function parses incoming message and processes it.

    :param message:
    :return: dict with response code
    """
    S_LOGGER.debug(f'Parsing message: {message}')
    if COMMAND in message and message[COMMAND] == ONLINE and TIMESTAMP in message \
            and USER in message and ACCOUNT_NAME in message[USER] \
            and message[USER][ACCOUNT_NAME] == 'guest':
        return {
            RESPONSE: 200
        }
    S_LOGGER.error('Incorrect message {message}. Bad request.')
    return {
        RESPONSE: 400,
        ERROR: 'Bad request'
    }


def main():
    """
    main function. Loading params from the command line:
        -p - port
        -a - address
    :return:
    """
    try:
        if '-p' in sys.argv:
            server_port = int(sys.argv[sys.argv.index('-p') + 1])
            S_LOGGER.info(f'Connection port specified: {server_port}')
        else:
            server_port = DEFAULT_PORT
            S_LOGGER.info(f'Using default port : {server_port}')
        if server_port <= 1024 and server_port > 65535:
            raise ValueError
    except IndexError:
        S_LOGGER.error("After '-p' option no port entered.")
        sys.exit(1)
    except ValueError:
        S_LOGGER.critical(f"Bad port number entered: {server_port} "
                          f"(must lay between 1024 and 65536).")
        sys.exit(1)
    try:
        if '-a' in sys.argv:
            server_address = sys.argv[sys.argv.index('-a') + 1]
            S_LOGGER.info(f'Connection address specified: {server_address}')
        else:
            server_address = ''  # DEFAULT_IP_ADDRESS # =''
            S_LOGGER.info('Using local address.')
    except IndexError:
        S_LOGGER.error('No address entered after -p param.')
        sys.exit(1)

    S_LOGGER.info(f'Starting server on ip-address: {server_address}, port: {server_port}')
    each_socket = socket(AF_INET, SOCK_STREAM)
    each_socket.bind((server_address, server_port))
    each_socket.listen(MAX_CONNECTIONS)

    while True:
        each_client_socket, each_client_address = each_socket.accept()
        S_LOGGER.info(f'Connection established. Client details: {each_client_address}.')
        try:
            client_message = get_message(each_client_socket)
            S_LOGGER.info(f'Received message {client_message} from client {each_client_address}.')
            server_response = parse_message(client_message)
            S_LOGGER.info(f'Server response to {each_client_address}: {server_response}.')
            send_message(each_client_socket, server_response)
            S_LOGGER.info('Closing connection')
            each_client_socket.close()
        except (ValueError, json.JSONDecodeError):
            S_LOGGER.error(f'Incorrect client message received. Can\'t decode message from '
                           f'{each_client_address}.')
            each_client_socket.close()

if __name__ == '__main__':
    main()
