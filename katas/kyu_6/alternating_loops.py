from itertools import izip_longest


def combine(*args):
    return [b for a in izip_longest(*args) for b in a if b]
