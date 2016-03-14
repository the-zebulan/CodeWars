def midpoint_sum(ints):
    for a in xrange(1, len(ints) - 1):
        if sum(ints[:a]) == sum(ints[a + 1:]):
            return a
