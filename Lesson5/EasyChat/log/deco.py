"""
module contents decorators implementing function logging
"""
import logging
import os
import sys
import traceback
import log.config.client_log_config
import log.config.server_log_config
try:
    if os.path.split(sys.argv[0])[1] == 'each_client.py':
        COMMON_LOGGER = logging.getLogger('each.client.log')
    elif os.path.split(sys.argv[0])[1] == 'each_server.py':
        COMMON_LOGGER = logging.getLogger('each.server.log')
    else:
        raise ValueError('Wrong module used with decorator from the module \'deco\'')

    def log(function):
        """
        Function implements logging wrapper for functions in modules:
            - each_client.py
            - each_server.py
        """
        def wrapper(*args, **kwargs):
            # getting current formatter
            old_formatter = COMMON_LOGGER.handlers[0].formatter._fmt
            # changing formatter to the new according to homework #6 requirements
            COMMON_LOGGER.handlers[0].setFormatter(logging.Formatter('%(asctime)-26s %(message)s'))
            res = function(*args, **kwargs)
            stack = traceback.extract_stack()
            COMMON_LOGGER.debug(f'Function {function.__name__} called with parameters '
                                f'{args, kwargs} from function {stack[-2][2]} with '
                                f'return value {res}. <Logged by Function decorator>')
            # setting back the previous formatter
            COMMON_LOGGER.handlers[0].setFormatter(logging.Formatter(old_formatter))
            return res
        return wrapper


    class Log():
        """
        Class implements logging wrapper for functions in modules:
            - each_client.py
            - each_server.py
        """
        def __call__(self, function):
            self.formatter = ''
            def wrapper(*args, **kwargs):
                self.formatter = COMMON_LOGGER.handlers[0].formatter._fmt
                COMMON_LOGGER.handlers[0].setFormatter(
                    logging.Formatter('%(asctime)-26s %(message)s')
                )
                res = function(*args, **kwargs)
                stack = traceback.extract_stack()
                COMMON_LOGGER.debug(f'Function {function.__name__} called with parameters'
                                    f' {args, kwargs} from function {stack[-2][2]} with '
                                    f'return value {res}. <Logged by Class decorator>')
                COMMON_LOGGER.handlers[0].setFormatter(logging.Formatter(self.formatter))
                return res
            return wrapper

        
    if __name__ == "__main__":
        print('main')

except ValueError as error:
    if os.path.split(sys.argv[0])[1] == 'deco.py':
        print('testing deco module')

