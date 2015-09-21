def get_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(xrange(a, b + 1))

assert get_sum(0, 1) == 1
assert get_sum(0, -1) == -1
