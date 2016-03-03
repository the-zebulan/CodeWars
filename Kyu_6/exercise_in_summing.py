def maximum_sum(values, n):
    values.sort()
    return sum(values[-n:])


def minimum_sum(values, n):
    values.sort()
    return sum(values[:n])

assert minimum_sum([5, 4, 3, 2, 1], 2) == 3
assert maximum_sum([5, 4, 3, 2, 1], 3) == 12
assert minimum_sum([5, 4, 3, 2, 1], 7) == 15
assert minimum_sum([], 3) == 0
