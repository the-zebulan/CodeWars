def midpoint_sum(ints):
    for a in xrange(1, len(ints) - 1):
        if sum(ints[:a]) == sum(ints[a + 1:]):
            return a

assert midpoint_sum([4, 1, 7, 9, 3, 9]) == 3
assert midpoint_sum([0, 0]) is None
assert midpoint_sum([0, 0, 1]) is None
assert midpoint_sum([1, 0, 1]) == 1
assert midpoint_sum([9, 0, 1, 2, 3, 4]) == 2
assert midpoint_sum([0, 0, 4, 0]) == 2
assert midpoint_sum([-10, 3, 7, 8, -6, -13, 21]) == 4
assert midpoint_sum([1, 1, 1, 1, -5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1]) ==  52
