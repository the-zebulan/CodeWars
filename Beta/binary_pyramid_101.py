BINARY = '{:b}'.format


def binary_piramid(m, n):
    """ piramid != pyramid, typo is from CodeWars """
    return BINARY(sum(int(BINARY(a)) for a in xrange(m, n + 1)))
