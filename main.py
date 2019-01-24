import flask
from typing import Dict, Tuple

from kdnfeed.feed import Feed

feed = Feed()


def serve(request: flask.Request) -> Tuple[bytes, int, Dict[str, str]]:
    return feed.feed(), 200, {'Content-Type': 'text/xml; charset=utf-8'}
