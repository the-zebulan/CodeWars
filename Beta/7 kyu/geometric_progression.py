def geometric_sequence_elements(a, r, n):
    return ', '.join(str(a * r ** i) for i in xrange(n))

assert geometric_sequence_elements(2, 3, 5) == '2, 6, 18, 54, 162'
assert geometric_sequence_elements(2, 2, 10) == \
    '2, 4, 8, 16, 32, 64, 128, 256, 512, 1024'
assert geometric_sequence_elements(1, -2, 10) == \
    '1, -2, 4, -8, 16, -32, 64, -128, 256, -512'
