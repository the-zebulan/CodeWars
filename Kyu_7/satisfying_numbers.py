from fractions import gcd


def smallest(n):
    return reduce(lambda a, b: (a * b) / gcd(a, b), xrange(1, n + 1), 1)
