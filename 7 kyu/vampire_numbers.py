def vampire_test(x, y):
    return sorted(str(x * y)) == sorted('{}{}'.format(x, y))

assert vampire_test(21, 6) is True
assert vampire_test(204, 615) is True
assert vampire_test(30, -51) is True
assert vampire_test(-246, -510) is False
assert vampire_test(210, 600) is True
