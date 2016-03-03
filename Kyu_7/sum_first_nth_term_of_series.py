def series_sum(n):
    return '{:.2f}'.format(sum(1.0 / a for a in xrange(1, n * 3, 3)))

assert series_sum(5) == '1.57'
assert series_sum(1) == '1.00'
assert series_sum(2) == '1.25'
assert series_sum(3) == '1.39'
