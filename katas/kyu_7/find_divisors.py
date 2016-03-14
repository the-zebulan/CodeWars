def divisors(n):
    return sum(n % a == 0 for a in xrange(1, n + 1))
