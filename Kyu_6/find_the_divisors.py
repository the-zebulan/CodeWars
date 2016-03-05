def divisors(num):
    return [a for a in xrange(2, num / 2 + 1) if num % a == 0] or \
           '{} is prime'.format(num)
