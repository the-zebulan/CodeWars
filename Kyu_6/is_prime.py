# def is_prime(n):
#     if n < 2 or any(n % i == 0 for i in xrange(2, int(n ** 0.5) + 1)):
#         return False
#     return True


def is_prime(n):
    return n > 1 and not any(n % i == 0 for i in xrange(2, int(n ** 0.5) + 1))
