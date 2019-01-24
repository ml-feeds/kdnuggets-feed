import time

from kdnfeed.feed import Feed

if __name__ == '__main__':
    try:
        print(Feed().feed().decode())
    except Exception:
        time.sleep(.01)  # Delay for logs to flush.
        raise
