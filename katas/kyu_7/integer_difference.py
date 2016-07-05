from collections import Counter


def int_diff(arr, n):
    cnts = Counter(arr)
    if n == 0:
        return sum(v * (v - 1) // 2 for v in cnts.values())
    return sum(v * cnts[k + n] for k, v in cnts.items())
