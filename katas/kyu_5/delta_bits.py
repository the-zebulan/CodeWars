from itertools import izip_longest


def convert_bits(a, b):
    binary = '{:b}'.format
    return sum(c != d for c, d in izip_longest(
        reversed(binary(a)), reversed(binary(b)), fillvalue='0'
    ))
