def seven(m):
    steps = 0
    while m > 99:
        q, r = divmod(m, 10)
        m = q - (2 * r)
        steps += 1
    return m, steps

assert seven(483) == (42, 1)
assert seven(371) == (35, 1)
assert seven(1603) == (7, 2)
assert seven(477557101) == (28, 7)
assert seven(0) == (0, 0)
