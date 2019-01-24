import flask

from kdnfeed.feed import feed


def serve(request: flask.Request) -> bytes:
    return feed(), 200, {'Content-Type': 'text/xml; charset=utf-8'}  # Alt: application/rss+xml; charset=utf-8
