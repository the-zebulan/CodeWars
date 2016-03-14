from collections import defaultdict


def greatest_distance(arr):
    indexes = defaultdict(list)
    for i, a in enumerate(arr):
        indexes[a].append(i)
    try:
        return max(b[-1] - b[0] for b in indexes.itervalues() if len(b) > 1)
    except ValueError:
        return 0
