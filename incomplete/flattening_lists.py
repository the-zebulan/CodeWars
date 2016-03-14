def flatten(lst):
    return [b for a in lst for b in a]


assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
assert flatten([[1], [2], [3], [4]]) == [1, 2, 3, 4]

print sum([[1], [2], [3], [4], [5]], [])  # only works for one level nested
print sum([[1], [2], [3], [4], [[5]]], [])  # doesn't flatten the 5
