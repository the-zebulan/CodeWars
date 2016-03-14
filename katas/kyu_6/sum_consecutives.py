from itertools import groupby


def sum_consecutives(nums):
    return [sum(g) for _, g in groupby(nums)]
