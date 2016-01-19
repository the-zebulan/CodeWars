ONE_ZERO = '10'


def stringy(size):
    return ''.join(ONE_ZERO[a % 2] for a in xrange(size))
    # return "10" * (size / 2) + "1" * (size % 2)


assert stringy(5) == '10101'
assert stringy(6) == '101010'
assert stringy(4) == '1010'
assert stringy(12) == '101010101010'
