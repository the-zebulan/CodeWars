from itertools import groupby


def ones_counter(nums):
    return [sum(g) for k, g in groupby(nums) if k]
