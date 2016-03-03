from collections import defaultdict


def greatest_distance(arr):
    indexes = defaultdict(list)
    for i, a in enumerate(arr):
        indexes[a].append(i)
    try:
        return max(b[-1] - b[0] for b in indexes.itervalues() if len(b) > 1)
    except ValueError:
        return 0


assert greatest_distance([0, 2, 1, 2, 4, 1]) == 3
assert greatest_distance([9, 7, 1, 2, 3, 7, 0, -1, -2]) == 4
assert greatest_distance([0, 7, 0, 2, 3, 7, 0, -1, -2]) == 6
assert greatest_distance([1, 2, 3, 4]) == 0
