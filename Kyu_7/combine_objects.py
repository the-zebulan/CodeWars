from collections import Counter


def combine(*args):
    return sum((Counter(a) for a in args), Counter())
