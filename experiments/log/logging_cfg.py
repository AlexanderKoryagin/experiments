import logging.config
import os

import yaml


def setup_logging(
        cfg_path='logging_cfg.yaml',
        log_level=None
):
    """Setup logging configuration."""
    if os.path.exists(cfg_path):
        with open(cfg_path, 'rt') as f:
            config = yaml.safe_load(f.read())

            if log_level is 'DEBUG':
                config['handlers']['console']['level'] = log_level
                config['handlers']['console']['formatter'] = log_level.lower()

        logging.config.dictConfig(config)
    else:
        raise IOError('No such file or directory: %s' % cfg_path)
