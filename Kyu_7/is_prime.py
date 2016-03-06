def is_prime(n):
    if n <= 1:
        return False
    for x in xrange(2, n):
        if n % x == 0:
            return False
    return True
