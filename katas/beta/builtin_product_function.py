from functools import reduce
from operator import mul


def product(iterable=(), start=1):
    return reduce(mul, iterable, start)


__builtins__.product = product
