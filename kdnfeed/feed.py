import logging
import urllib.request
from typing import Union
from xml.etree import ElementTree

from kdnfeed import config

config.configure_logging()

log = logging.getLogger(__name__)


def _is_blacklisted(item: ElementTree.Element) -> Union[tuple, bool]:
    item = {'title': item.findtext('title').lower(),
            'link': item.findtext('link').lower(),
            'category': [c.text.lower() for c in item.findall('category')],
            }
    for filter_tuple in config.BLACKLIST.itertuples(index=False, name='Filter'):
        operator = config.OPERATORS[filter_tuple.Operator]
        actual_value = item[filter_tuple.Field]
        blacklisted_value = filter_tuple.Value.lower()
        if filter_tuple.Field == 'category':
            for actual_individual_category in actual_value:
                if operator(actual_individual_category, blacklisted_value):
                    return filter_tuple
        else:
            if operator(actual_value, blacklisted_value):
                return filter_tuple
    return False


def feed() -> bytes:
    log.debug('Reading input feed.')
    text = urllib.request.urlopen(config.INPUT_FEED_URL).read()
    xml = ElementTree.fromstring(text)
    log.info('Received input feed of size %s bytes with %s items.', len(text), len(xml.findall('./channel/item')))

    channel = next(xml.iter('channel'))
    for item in channel.iter('item'):
        title = item.findtext('title')
        guid = item.findtext('guid')
        filter_status = _is_blacklisted(item)
        if filter_status:
            channel.remove(item)
            log.debug('❌ Removed %s "%s" as its %s %s "%s".\n',
                      guid, title, filter_status.Field, filter_status.Operator, filter_status.Value)
        else:
            log.debug('✅ Approved %s "%s" having categories: %s\n',
                      guid, title, ', '.join(c.text for c in item.findall('category')))
    text = ElementTree.tostring(xml)
    log.info('Generated output feed of size %s bytes with %s items.', len(text), len(xml.findall('./channel/item')))
    return text
