def proper_divisors_sum(n):
    return sum(a for a in xrange(1, n) if not n % a)


def amicable_numbers(a, b):
    return proper_divisors_sum(a) == b and proper_divisors_sum(b) == a


# def amicable_numbers(a, b):
#     # this works after multiple submissions to get lucky on random inputs
#     return sum(c for c in xrange(1, a) if not a % c) == b
