from collections import Counter


def find_dup(arr):
    return Counter(arr).most_common(1)[0][0]
