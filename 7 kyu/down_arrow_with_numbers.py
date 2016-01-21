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


assert get_a_down_arrow_of(10) == \
    '1234567890987654321\n 12345678987654321\n  123456787654321\n' \
    '   1234567654321\n    12345654321\n     123454321\n      1234321\n' \
    '       12321\n        121\n         1'
assert get_a_down_arrow_of(0) == ''
assert get_a_down_arrow_of(-5) == ''
assert get_a_down_arrow_of(3) == '12321\n 121\n  1'
assert get_a_down_arrow_of(5) == '123454321\n 1234321\n  12321\n   121\n    1'
