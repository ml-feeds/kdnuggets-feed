import time

from kdnfeed.feed import feed

if __name__ == '__main__':
    try:
        print(feed().decode())
    except Exception:
        time.sleep(.01)  # Delay for logs to flush.
        raise
