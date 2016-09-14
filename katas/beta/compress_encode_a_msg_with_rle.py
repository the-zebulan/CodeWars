from itertools import groupby


def encode(s):
    return ''.join(k + str(sum(1 for _ in g)) for k, g in groupby(s))
