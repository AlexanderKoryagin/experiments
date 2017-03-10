import logging

import logging_cfg
from some_module import DoSomething


LOGGER = logging.getLogger(__name__)


if __name__ == "__main__":

    logging_cfg.setup_logging()

    for x in range(0, 5):
        LOGGER.debug('Info debug %s' % x)
        LOGGER.info('Info numb %s' % x)
        LOGGER.warn('Warning numb %s' % x)
        LOGGER.error('Error numb %s' % x)
        LOGGER.critical('Critical numb %s' % x)

    a = DoSomething
    a()
