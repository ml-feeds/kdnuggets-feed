import logging.config
from pathlib import Path

import pandas as pd


def configure_logging() -> None:
    path = Path(__file__).with_name('logging.conf')
    logging.config.fileConfig(path)
    log = logging.getLogger(__name__)
    log.debug('Logging is configured.')


BLACKLIST_PATH = Path(__file__).with_name('blacklist.csv')
BLACKLIST = pd.read_csv(BLACKLIST_PATH)
INPUT_FEED_URL = 'https://www.kdnuggets.com/feed'
