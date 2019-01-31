import logging
from pathlib import Path
from resource import getpagesize

from descriptors import classproperty

from kdnuggets.util.humanize import humanize_bytes

log = logging.getLogger(__name__)


class MemUse:
    _PAGESIZE = getpagesize()
    _PATH = Path('/proc/self/statm')

    def __init__(self):
        self._initial_use = self._current_use

    @classproperty
    def _current_use(cls) -> int:
        """Return the current resident set size in bytes."""
        # Ref: https://stackoverflow.com/a/53486808/
        # statm columns are: size resident shared text lib data dt
        statm = cls._PATH.read_text()
        fields = statm.split()
        return int(fields[1]) * cls._PAGESIZE

    @property
    def current_use_humanized(self) -> str:
        return humanize_bytes(self._current_use)

    @property
    def delta_use_humanized(self) -> str:
        return humanize_bytes(self._current_use - self._initial_use)

    def log_use(self) -> None:
        log.info('Current memory use is %s and delta use since original is %s.',
                 self.current_use_humanized, self.delta_use_humanized)


