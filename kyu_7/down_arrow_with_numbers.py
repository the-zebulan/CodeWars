from itertools import chain

DIGITS = '1234567890'


def get_a_down_arrow_of(n):
    result = []
    for a in xrange(n):
        nums = ''.join(DIGITS[a % 10] for a in
                       chain(xrange(n), xrange(n - 2, -1, -1)))
        result.append('{:>{}}'.format(nums, a + len(nums)))
        n -= 1
    return '\n'.join(result)
