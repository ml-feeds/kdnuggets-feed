import flask


def serve(request: flask.Request) -> bytes:
    return 'yes really'.encode()
