from itertools import izip_longest


def createDict(keys, values):
    if len(keys) > len(values):
        return dict(izip_longest(keys, values, fillvalue=None))
    return dict(zip(keys, values))

assert createDict(['a', 'b', 'c', 'd'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3, 'd': None}
assert createDict(['a', 'b', 'c'], [1, 2, 3, 4]), {'a': 1, 'b': 2, 'c': 3}
