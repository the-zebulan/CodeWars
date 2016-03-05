def multiplication_table(row, col):
    return [range(a, a * col + 1, a) for a in xrange(1, row + 1)]
