from collections import Counter


def find_dup(arr):
    return Counter(arr).most_common(1)[0][0]

assert find_dup([5, 4, 3, 2, 1, 1]) == 1
assert find_dup([1, 3, 2, 5, 4, 5, 7, 6]) == 5
