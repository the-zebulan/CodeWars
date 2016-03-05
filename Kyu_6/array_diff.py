def array_diff(a, b):
    b = set(b)
    return [c for c in a if c not in b]
