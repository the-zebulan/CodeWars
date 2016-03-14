def is_prime(n):
    return n > 1 and all(n % i for i in xrange(2, int(n ** 0.5) + 1))


def sexy_prime(x, y):
    return abs(x - y) == 6 and is_prime(x) and is_prime(y)
