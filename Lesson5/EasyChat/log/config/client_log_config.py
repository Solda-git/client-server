import logging
import os
from lib.settings import LOG_LEVEL

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(os.path.split(PATH)[0], 'logs', 'client.log')

CLNT_LOG = logging.getLogger('each.client.log')
CLNT_HANDLER = logging.FileHandler(PATH, encoding='utf-8')
CLNT_HANDLER.setLevel(LOG_LEVEL)
CLNT_FORMATTER = logging.Formatter('%(levelname)-10s %(module)-20s %(message)s')
CLNT_HANDLER.setFormatter(CLNT_FORMATTER)
CLNT_LOG.addHandler(CLNT_HANDLER)
CLNT_LOG.setLevel(LOG_LEVEL)

if __name__ == '__main__':
    CLNT_LOG.debug('Critical record')
    CLNT_LOG.info('Info record')
    CLNT_LOG.warning('Warning record')
    CLNT_LOG.error('Error record')
    CLNT_LOG.critical("Critical record")

