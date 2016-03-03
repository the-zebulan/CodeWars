from itertools import izip_longest


def combine(*args):
    return [b for a in izip_longest(*args) for b in a if b]

assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
assert combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) \
    == ['a', 1, 'b', 2, 'c', 3, 4, 5]
assert combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) \
    == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
