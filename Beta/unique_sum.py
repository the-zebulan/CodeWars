def unique_sum(lst):
    return sum(set(lst))


assert unique_sum([1, 2, 3]) == 6
assert unique_sum([1, 3, 8, 1, 8]) == 12
assert unique_sum([-1, -1, 5, 2, -7]) == -1
