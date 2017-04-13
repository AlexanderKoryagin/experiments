import argparse
import logging

import logging_cfg
from some_module import DoSomething


LOGGER = logging.getLogger(__name__)


def get_args():
    """Read script arguments."""
    parser = argparse.ArgumentParser(
        description="Experiments with logging."
    )
    parser.add_argument(
        "--debug", '--D',
        action="store_true",
        default=False,
        help="console logger debug mode ON"
    )
    return parser.parse_args()


if __name__ == "__main__":

    args = get_args()

    log_level = 'DEBUG' if args.debug else None
    logging_cfg.setup_logging(
        log_level=log_level
    )

    for x in range(0, 5):
        LOGGER.debug('Info debug %s', x)
        LOGGER.info('Info numb %s', x)
        LOGGER.warn('Warning numb %s', x)
        LOGGER.error('Error numb %s', x)
        LOGGER.critical('Critical numb %s', x)

    a = DoSomething
    a()
