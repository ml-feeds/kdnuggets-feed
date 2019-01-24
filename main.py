import flask

from kdnfeed.feed import feed


def serve(request: flask.Request) -> bytes:
    return feed()
