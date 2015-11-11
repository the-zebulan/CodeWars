def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000


assert past(0, 1, 1) == 61000
assert past(1, 1, 1) == 3661000
assert past(0, 0, 0) == 0
assert past(1, 0, 1) == 3601000
assert past(1, 0, 0) == 3600000
