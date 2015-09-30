BINARY = '{:b}'.format


def binary_piramid(m, n):
    """ piramid != pyramid, typo is from CodeWars """
    return BINARY(sum(int(BINARY(a)) for a in xrange(m, n + 1)))

assert binary_piramid(1, 4) == '1111010'
assert binary_piramid(1, 6) == '101001101'
assert binary_piramid(6, 20) == '1110010110100011'
assert binary_piramid(21, 60) == '1100000100010001010100'
