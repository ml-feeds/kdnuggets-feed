import logging
from typing import Dict, Tuple

import flask

from kdnuggets.feed import Feed
from kdnuggets.util.resource import MemUse

log = logging.getLogger(__name__)
feed = Feed()
mem = MemUse()


def serve(request: flask.Request) -> Tuple[bytes, int, Dict[str, str]]:
    hget = request.headers.get
    log.info('Received request from %s from %s, %s, %s.', hget('X-Appengine-User-Ip'),
             hget('X-Appengine-City'), hget('X-Appengine-Region'), hget('X-Appengine-Country'))
    output = feed.fee()
    mem.log_use()
    return output, 200, {'Content-Type': 'text/xml; charset=utf-8'}
