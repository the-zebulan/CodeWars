from re import escape, split


def multiple_split(s, delimiters=()):
    if not s:
        return []
    if not delimiters:
        return [s]
    return filter(None, split(r'[{}]'.format(escape(''.join(delimiters))), s))
