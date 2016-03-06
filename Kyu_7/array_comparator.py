def hashable(v):
    return set(tuple(a) if isinstance(a, list) else a for a in v)


def match_arrays(v, r):
    return len(hashable(v).intersection(hashable(r)))
