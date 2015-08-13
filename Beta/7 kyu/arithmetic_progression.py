def arithmetic_sequence_elements(a, r, n):
    return ', '.join(str(a + b * r) for b in xrange(n))

assert arithmetic_sequence_elements(1, 2, 5) == '1, 3, 5, 7, 9'
assert arithmetic_sequence_elements(1, -3, 10) == \
    '1, -2, -5, -8, -11, -14, -17, -20, -23, -26'
