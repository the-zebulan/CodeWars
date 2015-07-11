def plural(n):
    return n != 1

assert plural(0) is True
assert plural(0.5) is True
assert plural(1) is False
assert plural(100) is True
