from functools import reduce
from operator import mul


def product(iterable=(), start=1):
    """ kata currently supports only Python 3.4.3 """
    return reduce(mul, iterable, start)


# __builtins__.product = product
