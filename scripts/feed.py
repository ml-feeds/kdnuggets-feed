import logging
import time

from kdnfeed.feed import Feed

log = logging.getLogger(__name__)

if __name__ == '__main__':
    feed = Feed()
    try:
        output = feed.feed()
        print(output.decode())

        log.info('Testing cache.')
        assert feed.feed() == output
        log.info('Tested cache.')
    except Exception:
        time.sleep(.01)  # Delay for logs to flush.
        raise
