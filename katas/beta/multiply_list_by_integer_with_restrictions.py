from operator import mul


def multiply(n, l):
    return map(lambda a: mul(a, n), l)
