def min_max(lst):
    a = sorted(len(b) for b in lst)
    return a[0], a[-1]


def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    a, b = min_max(a1)
    c, d = min_max(a2)
    return max(abs(d - a), abs(b - c))
