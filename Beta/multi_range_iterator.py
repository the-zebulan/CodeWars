from itertools import product


def multiiter(*args):
    return product(*(xrange(b) for b in args))


assert list(multiiter(0)) == []
assert list(multiiter(2)) == [(0,), (1,)]
assert list(multiiter(2, 3)) == \
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
assert list(multiiter(3, 2)) == \
    [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
