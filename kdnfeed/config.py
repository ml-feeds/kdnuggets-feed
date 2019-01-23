import logging.config
from pathlib import Path


def configure_logging() -> None:
    path = Path(__file__).with_name('logging.conf')
    logging.config.fileConfig(path)
    log = logging.getLogger(__name__)
    log.info('Logging is configured.')


INPUT_FEED_URL = 'https://www.kdnuggets.com/feed'
OUTPUT_FEED_DESCRIPTION = 'Filtered KDnuggets RSS feed (unofficial)'
OUTPUT_FEED_LINK = 'https://www.kdnuggets.com'
OUTPUT_FEED_TITLE = 'KDnuggets filtered (unofficial)'
