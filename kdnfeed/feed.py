from types import SimpleNamespace

from feedgen.feed import FeedGenerator
from riko.collections import SyncPipe

import kdnfeed.config as config

config.configure_logging()


def feed() -> bytes:
    pipe = SyncPipe('fetch', conf={'url': config.INPUT_FEED_URL}) \
        .sort(conf={'rule': {'sort_key': 'published_parsed', 'sort_dir': 'desc'}})

    output_feed = FeedGenerator()
    output_feed.title(config.OUTPUT_FEED_TITLE)
    output_feed.link(href=config.OUTPUT_FEED_LINK, rel='self')
    output_feed.description(config.OUTPUT_FEED_DESCRIPTION)

    for pipe_entry in pipe.output:
        pipe_entry = SimpleNamespace(**pipe_entry)  # For dot access of attributes rather than dict access.
        feed_entry = output_feed.add_entry()
        feed_entry.title(pipe_entry.title)
        feed_entry.link(href=pipe_entry.link)
        feed_entry.guid(pipe_entry.id, permalink=pipe_entry.id.startswith(('https://', 'http://')))
        feed_entry.summary(pipe_entry.summary)
        feed_entry.category([{'term': tag['term']} for tag in pipe_entry.tags])  # Doesn't work w/ just pipe_entry.tags
        feed_entry.published(pipe_entry.published)

    output = output_feed.rss_str(pretty=True)
    return output


if __name__ == '__main__':
    print(feed().decode())
