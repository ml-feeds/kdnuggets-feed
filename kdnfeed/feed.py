import logging
import urllib.request
import xml.etree.ElementTree as ET

import kdnfeed.config as config

config.configure_logging()

log = logging.getLogger(__name__)


def feed() -> bytes:
    log.debug('Reading input feed.')
    xml = urllib.request.urlopen(config.INPUT_FEED_URL).read()
    log.info('Read input feed of size %s bytes.', len(xml))

    xml = ET.fromstring(xml)
    channel = next(xml.iter('channel'))
    for item in channel.iter('item'):
        pass
    xml = ET.tostring(xml)
    log.info('Generated output feed of size %s bytes.', len(xml))
    return xml
