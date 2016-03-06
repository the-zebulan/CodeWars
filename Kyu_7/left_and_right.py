def left(string, i=1):
    return string[:string.index(i) if isinstance(i, str) else i]


def right(string, i=1):
    i = string[::-1].index(i[::-1]) if isinstance(i, str) else i
    return string[-i:] if not i == 0 else ""
