from collections import Counter


def dominator(arr):
    if not arr:
        return -1
    k, v = Counter(arr).most_common(1)[0]
    return k if v > len(arr) / 2 else -1
