def multiplication_table(row, col):
    return [range(a, a * col + 1, a) for a in xrange(1, row + 1)]

assert multiplication_table(2, 2), [[1, 2], [2, 4]]
assert multiplication_table(3, 3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
