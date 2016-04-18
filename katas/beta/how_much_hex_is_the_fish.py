VALID = frozenset('abcdefABCDEF')


def fisHex(s):
    return reduce(lambda b, c: b ^ c, (int(a, 16) for a in s if a in VALID), 0)
