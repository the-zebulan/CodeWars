from itertools import izip


def gps(s, x):
    return 0 if len(x) <= 1 else \
        int(max(((b - a) / s) * 3600 for a, b in izip(x, x[1:])))
