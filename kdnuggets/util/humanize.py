from humanize import naturalsize


def _humanize_bytes(num_bytes: int) -> str:
    return naturalsize(num_bytes, gnu=True, format='%.0f')


def humanize_bytes(num_bytes: int) -> str:
    return _humanize_bytes(num_bytes) if num_bytes >= 0 else f"-{_humanize_bytes(-num_bytes)}"


def humanize_len(text: bytes) -> str:
    return humanize_bytes(len(text))
