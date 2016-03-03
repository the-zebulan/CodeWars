def divisors(n):
    return sum(n % a == 0 for a in xrange(1, n + 1))

assert divisors(1) == 1
assert divisors(4) == 3
