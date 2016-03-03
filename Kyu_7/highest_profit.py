def min_max(lst):
    lst.sort()
    return [lst[0], lst[-1]]

assert min_max([1, 2, 3, 4, 5]) == [1, 5]
assert min_max([2334454, 5]) == [5, 2334454]
assert min_max([1]) == [1, 1]
