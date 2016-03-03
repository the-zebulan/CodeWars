def divisors(num):
    return [a for a in xrange(2, num / 2 + 1) if num % a == 0] or \
           '{} is prime'.format(num)

assert divisors(12) == [2, 3, 4, 6]
assert divisors(25) == [5]
assert divisors(13) == '13 is prime'
assert divisors(15) == [3, 5]
