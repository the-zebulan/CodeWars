def digitize(n):
    return map(int, str(n))

assert digitize(123) == [1, 2, 3]
assert digitize(1) == [1]
assert digitize(0) == [0]
assert digitize(1230) == [1, 2, 3, 0]
assert digitize(8675309) == [8, 6, 7, 5, 3, 0, 9]
