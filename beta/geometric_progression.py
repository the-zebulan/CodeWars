def geometric_sequence_elements(a, r, n):
    return ', '.join(str(a * r ** i) for i in xrange(n))
