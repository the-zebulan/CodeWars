from itertools import product


def multiiter(*args):
    return product(*(xrange(b) for b in args))
