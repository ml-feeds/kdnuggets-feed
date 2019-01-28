import logging

from kdnuggets import config

config.configure_logging()

log = logging.getLogger(__name__)

df = config.BLACKLIST.copy()
df = df.sort_values(df.columns.tolist()).drop_duplicates()
if not df.equals(config.BLACKLIST):
    df.to_csv(config.BLACKLIST_PATH, index=False)
    log.info('Sorted the blacklist file.')
else:
    log.info('The blacklist file is already sorted.')
