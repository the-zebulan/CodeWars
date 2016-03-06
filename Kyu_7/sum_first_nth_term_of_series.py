def series_sum(n):
    return '{:.2f}'.format(sum(1.0 / a for a in xrange(1, n * 3, 3)))
