from itertools import chain, izip
from string import ascii_lowercase as low, ascii_uppercase as up, digits

KEYS = {a: i for i, a in enumerate(chain(
    up, low, chain.from_iterable(izip(xrange(10), digits))))}


def unusual_sort(array):
    return sorted(array, key=lambda a: KEYS[a])
