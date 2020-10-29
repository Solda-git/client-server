import json
import sys
from distutils import command
from socket import SOCK_STREAM, AF_INET, socket

from lib.routines import get_message, send_message
from lib.settings import MAX_CONNECTIONS, COMMAND, TIMESTAMP, USER, ACCOUNT_NAME, ONLINE, DEFAULT_PORT, \
    DEFAULT_IP_ADDRESS, RESPONSE, ERROR


def parse_message(message):
    """
    function parses incoming message and processes it.

    :param message:
    :return: dict with response code
    """
    if COMMAND in message and message[COMMAND] == ONLINE and TIMESTAMP in message \
        and USER in message and message[USER][ACCOUNT_NAME] == 'guest':
        return {
            RESPONSE: 200
        }
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
            server_port = int(sys.argv[sys.argv.index('-p')+1])
            print(server_port);
        else:
            server_port = DEFAULT_PORT
        if server_port <= 1024 and server_port > 65535:
            raise ValueError
    except IndexError:
        print("After '-p' option input port value.")
        sys.exit(1)
    except ValueError:
        print("Port value must be between 1024 and 65536.")
        sys.exit(1)
    try:
        if '-a' in sys.argv:
            server_address = sys.argv[sys.argv.index('-a') + 1]
            print(server_address)
        else:
            server_address = '' #DEFAULT_IP_ADDRESS # =''
    except IndexError:
        print("After '-a' option input address value to be listened by the server")
        sys.exit(1)

    each_socket = socket(AF_INET, SOCK_STREAM)
    each_socket.bind((server_address, server_port))
    each_socket.listen(MAX_CONNECTIONS)

    while True:
        each_client_socket, each_client_address = each_socket.accept()
        try:
            client_message = get_message(each_client_socket)
            print(client_message)
            server_response = parse_message(client_message)
            send_message(each_client_socket, server_response)
            each_client_socket.close()
        except (ValueError, json.JSONDecodeError):
            print('Incorrect cliemt message received.')
            each_client_socket.close()


if __name__ == '__main__':
    main()
