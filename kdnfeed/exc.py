import logging

log = logging.getLogger(__name__)


class Error(Exception):
    def __init__(self, msg: str):
        log.error(msg)
        super().__init__(msg)
