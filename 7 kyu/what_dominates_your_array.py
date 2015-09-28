from collections import Counter


def dominator(arr):
    if not arr:
        return -1
    k, v = Counter(arr).most_common(1)[0]
    return k if v > len(arr) / 2 else -1

assert dominator([3, 4, 3, 2, 3, 1, 3, 3]) == 3
assert dominator([1, 2, 3, 4, 5]) == -1
assert dominator([1, 1, 1, 2, 2, 2]) == -1
assert dominator([1, 1, 1, 2, 2, 2, 2]) == 2
assert dominator([]) == -1
