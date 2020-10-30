import json
import sys
from socket import socket, AF_INET, SOCK_STREAM
from time import time

from lib.routines import send_message, get_message
from lib.settings import ONLINE, COMMAND, TIMESTAMP, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP_ADDRESS, \
    DEFAULT_PORT


def make_online(account='guest'):
    """
    function generates request making chat user online

    :param account:
    :return:
    """
    return {
        COMMAND: ONLINE,
        TIMESTAMP: time(),
        USER: {
            ACCOUNT_NAME: account
        }
    }


def parse_server_answer(message):
    """
    function processes message from the server
    :param message:
    :return: dict with status
    """
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
    except ValueError:
        print("Port value must be between 1024 and 65536.")
        print(each_server_port)
        sys.exit(1)

    print(f'each_server_address = {each_server_address}, each_server_port = {each_server_port}')

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((each_server_address, each_server_port))
    send_message(client_socket, make_online())
    try:
        print(parse_server_answer(get_message(client_socket)))
    except (ValueError, json.JSONDecodeError):
        print("Can't decode server message")


if __name__ == '__main__':
    main()
