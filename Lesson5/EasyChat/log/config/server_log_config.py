import logging
import logging.handlers
import os
import sys
from lib.settings import LOG_LEVEL

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(os.path.split(PATH)[0], 'logs', 'srv.log')

SRV_LOG = logging.getLogger('each.server.log')
SRV_HANDLER = logging.handlers.TimedRotatingFileHandler(
    PATH,
    encoding='utf8',
    interval=1,
    when='D'
)

# SRV_HANDLER = logging.StreamHandler(sys.stdout)
SRV_HANDLER.setLevel(LOG_LEVEL)
SRV_FORMATTER = logging.Formatter('%(asctime)-26s %(levelname)-10s %(module)-20s %(message)s')
SRV_HANDLER.setFormatter(SRV_FORMATTER)
SRV_LOG.addHandler(SRV_HANDLER)
SRV_LOG.setLevel(LOG_LEVEL)


# Parameters:
#
# PARAMS = {
#     'host': 'localhost',
#     'port': 50
# }
#
# log.info('Connection params: %(host)s, %(port)d', PARAMS)


if __name__ == '__main__':
    SRV_LOG.debug('Critical record rotating + LOG_INFO')
    SRV_LOG.info('Info record rotating')
    SRV_LOG.warning('Warning record rotating')
    SRV_LOG.error('Error record rotating')
    SRV_LOG.critical("Critical record rotating")
