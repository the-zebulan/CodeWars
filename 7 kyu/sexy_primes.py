def is_prime(n):
    return n > 1 and all(n % i for i in xrange(2, int(n ** 0.5) + 1))


def sexy_prime(x, y):
    return is_prime(x) and is_prime(y) and abs(x - y) == 6


assert sexy_prime(5, 11) is True
assert sexy_prime(13, 19) is True
assert sexy_prime(83, 89) is True
assert sexy_prime(1, 11) is False
