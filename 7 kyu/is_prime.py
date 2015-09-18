def is_prime(n):
    if n <= 1:
        return False
    for x in xrange(2, n):
        if n % x == 0:
            return False
    return True

assert is_prime(0) is False
assert is_prime(1) is False
assert is_prime(2) is True
assert is_prime(11) is True
assert is_prime(12) is False
