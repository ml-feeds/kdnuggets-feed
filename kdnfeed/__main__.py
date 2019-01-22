import time

from mypackage.config import configure_logging

configure_logging()

if __name__ == '__main__':
    try:
        pass
    except Exception:
        time.sleep(.01)  # Delay for logs to flush.
        raise
