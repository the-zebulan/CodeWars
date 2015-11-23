from itertools import groupby


def sum_consecutives(nums):
    return [sum(g) for _, g in groupby(nums)]


assert sum_consecutives([1, 4, 4, 4, 0, 4, 3, 3, 1]) == [1, 12, 0, 4, 6, 1]
assert sum_consecutives([1, 1, 7, 7, 3]) == [2, 14, 3]
assert sum_consecutives([-5, -5, 7, 7, 12, 0]) == [-10, 14, 12, 0]
assert sum_consecutives([3, 3, 3, 3, 1]) == [12, 1]
