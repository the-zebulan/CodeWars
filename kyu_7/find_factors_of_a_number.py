def factors(x):
    if x <= 0 or not isinstance(x, int):
        return -1
    seen = set()
    for a in xrange(1, int(x ** 0.5) + 1):
        if not x % a:
            seen.add(a)
            seen.add(x / a)
    return sorted(seen, reverse=True)
