



def make_online(account='guest'):
    """
    function generates request making chat user online

    :param account:
    :return:
    """
    return {
        COMMAND: ONLINE,
        TIMESTAMP: time(),
        USER = {
            ACCOUNT_NAME = account
        }
    }

def main():
   """
   main function. Loading params from the command line:
        -p - port
        -a - address
   :return:
   """


if __name__ == '__main__':
    main()