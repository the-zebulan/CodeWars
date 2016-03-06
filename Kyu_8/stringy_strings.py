ONE_ZERO = '10'


def stringy(size):
    return ''.join(ONE_ZERO[a % 2] for a in xrange(size))
    # return "10" * (size / 2) + "1" * (size % 2)
