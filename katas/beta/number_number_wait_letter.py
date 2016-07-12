from itertools import cycle
from operator import add, mul, sub, truediv


def do_math(s):
    ops = cycle((add, sub, mul, truediv))
    pairs = []
    for i, a in enumerate(s.split()):
        current = sorted(a, key=str.isalpha)
        pairs.append(((current.pop(), i), int(''.join(current))))
    return round(reduce(lambda prev, curr: next(ops)(prev, curr),
                        (num for _, num in sorted(pairs))))
