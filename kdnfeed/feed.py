import logging
import random   # TODO: Remove after actual filters are implemented.
import urllib.request
import xml.etree.ElementTree as ET

import kdnfeed.config as config

config.configure_logging()

log = logging.getLogger(__name__)


def feed() -> bytes:
    log.debug('Reading input feed.')
    text = urllib.request.urlopen(config.INPUT_FEED_URL).read()
    xml = ET.fromstring(text)
    log.info('Received input feed of size %s bytes with %s items.', len(text), len(xml.findall('./channel/item')))

    channel = next(xml.iter('channel'))
    for item in channel.iter('item'):
        if random.getrandbits(1):
            channel.remove(item)
    text = ET.tostring(xml)
    log.info('Generated output feed of size %s bytes with %s items.', len(text), len(xml.findall('./channel/item')))
    return text
