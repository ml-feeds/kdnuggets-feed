import flask
from typing import Dict, Tuple

from kdnfeed.feed import feed


def serve(request: flask.Request) -> Tuple[bytes, int, Dict[str, str]]:
    return feed(), 200, {'Content-Type': 'text/xml; charset=utf-8'}
