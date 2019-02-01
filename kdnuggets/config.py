import datetime
import logging.config
import os
from pathlib import Path

import operator
import pandas as pd


def configure_logging() -> None:
    logging.config.dictConfig(LOGGING)
    log = logging.getLogger(__name__)
    log.debug('Logging is configured.')


BLACKLIST_PATH = Path(__file__).with_name('blacklist.csv')
BLACKLIST = pd.read_csv(BLACKLIST_PATH)
CACHE_TTL = datetime.timedelta(hours=3).total_seconds()
FEED_DESCRIPTION_SUFFIX = '. As a disclaimer, this is an unofficial feed and has no affiliation with KDnuggets.'
FEED_TITLE_SUFFIX = ' (unofficial)'
INPUT_FEED_URL = 'https://www.kdnuggets.com/feed'
ON_SERVERLESS = bool(os.getenv('GCLOUD_PROJECT'))
OPERATORS = {
    'contains': operator.contains,
    'equals': operator.eq,
    'endswith': str.endswith,
    'startswith': str.startswith,
}
PACKAGE_NAME = Path(__file__).parent.stem
REPO_URL = 'https://github.com/ml-feeds/kdnuggets-feed'

LOGGING = {  # Ref: https://docs.python.org/3/howto/logging.html#configuring-logging
    'version': 1,
    'formatters': {
        'detailed': {
            'format': '[%(relativeCreated)i] %(name)s:%(lineno)d:%(funcName)s:%(levelname)s: %(message)s',
        },
        'serverless': {
            'format': '%(thread)x:%(name)s:%(lineno)d:%(funcName)s:%(levelname)s: %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'serverless' if ON_SERVERLESS else 'detailed',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        PACKAGE_NAME: {
            'level': 'INFO' if ON_SERVERLESS else 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        '': {
            'level': 'DEBUG',
            'handlers': ['console'],
         },
    },
}

