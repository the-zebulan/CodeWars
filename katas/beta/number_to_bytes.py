from math import ceil


def to_bytes(n):
    binary = '{:b}'.format(n)
    width = int(ceil(len(binary) / 8.0) * 8)
    padded = binary.zfill(width)
    return [padded[a:a + 8] for a in xrange(0, width, 8)]
