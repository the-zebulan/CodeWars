def factors(x):
    if x <= 0 or not isinstance(x, int):
        return -1
    seen = set()
    for a in xrange(1, int(x ** 0.5) + 1):
        if not x % a:
            seen.add(a)
            seen.add(x / a)
    return sorted(seen, reverse=True)


assert factors(-4) == -1
assert factors(0) == -1
assert factors(-12) == -1
assert factors('a') == -1
assert factors(4.5) == -1
assert factors('hello world') == -1
assert factors(54) == [54, 27, 18, 9, 6, 3, 2, 1]
assert factors(49) == [49, 7, 1]
assert factors(1) == [1]
