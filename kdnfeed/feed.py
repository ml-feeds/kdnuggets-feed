from functools import lru_cache
import logging
import time
from urllib.request import urlopen
from typing import Union
from xml.etree import ElementTree

from cachetools.func import ttl_cache
from humanize import naturalsize

from kdnfeed import config

config.configure_logging()

log = logging.getLogger(__name__)


class Feed:
    def __init__(self):
        self._blacklist = config.BLACKLIST.copy()
        self._blacklist['Value'] = self._blacklist['Value'].str.lower()  # For case-insensitive comparison.
        self._is_debug_logged = log.isEnabledFor(logging.DEBUG)

    def _is_blacklisted(self, item: ElementTree.Element) -> Union[tuple, bool]:
        item = {'title': item.findtext('title').lower(),  # type: ignore
                'link': item.findtext('link').lower(),
                'category': [c.text.lower() for c in item.findall('category')],  # type: ignore
                }
        for filter_tuple in self._blacklist.itertuples(index=False, name='Filter'):
            operator = config.OPERATORS[filter_tuple.Operator]
            actual_value = item[filter_tuple.Field]
            blacklisted_value = filter_tuple.Value
            if filter_tuple.Field == 'category':
                for actual_individual_category in actual_value:
                    if operator(actual_individual_category, blacklisted_value):  # type: ignore
                        return filter_tuple
            else:
                if operator(actual_value, blacklisted_value):  # type: ignore
                    return filter_tuple
        return False

    @lru_cache(maxsize=1)
    def _output(self, text: str) -> str:
        xml = ElementTree.fromstring(text)
        log.info('Input feed has %s items.', len(xml.findall('./channel/item')))

        is_debug_logged = self._is_debug_logged
        channel = next(xml.iter('channel'))
        for item in list(channel.iter('item')):  # https://stackoverflow.com/a/19419905/
            title = item.findtext('title')
            guid = item.findtext('guid')
            filter_status = self._is_blacklisted(item)
            if filter_status:
                channel.remove(item)
            if is_debug_logged:
                if filter_status:
                    log.debug('❌ Removed %s "%s" as its %s %s "%s".\n',
                              guid, title, filter_status.Field, filter_status.Operator, filter_status.Value)  # type: ignore
                else:
                    log.debug('✅ Approved %s "%s" having categories: %s\n',
                              guid, title, ', '.join(c.text for c in item.findall('category')))  # type: ignore

        log.info('Output feed has %s items.', len(xml.findall('./channel/item')))
        text = ElementTree.tostring(xml)
        return text

    @ttl_cache(maxsize=1, ttl=config.CACHE_TTL, timer=time.monotonic)
    def feed(self) -> bytes:
        log.debug('Reading input feed.')
        text = urlopen(config.INPUT_FEED_URL).read()
        log.info('Input feed has size %s.', humanize_len(text))
        text = self._output(text)
        log.info('Output feed has size %s.', humanize_len(text))
        return text


def humanize_len(text: str) -> str:
    return naturalsize(len(text), gnu=True, format='%.0f')
