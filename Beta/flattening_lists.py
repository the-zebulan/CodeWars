def flatten(lst):
    return [b for a in lst for b in a]


assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
assert flatten([[1], [2], [3], [4]]) == [1, 2, 3, 4]
