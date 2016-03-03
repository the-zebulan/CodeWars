from fractions import gcd


def smallest(n):
    return reduce(lambda a, b: (a * b) / gcd(a, b), xrange(1, n + 1), 1)

assert smallest(1) == 1
assert smallest(2) == 2
assert smallest(3) == 6
assert smallest(4) == 12
assert smallest(5) == 60
assert smallest(6) == 60
assert smallest(7) == 420
assert smallest(8) == 840
assert smallest(9) == 2520
assert smallest(10) == 2520
