def array_diff(a, b):
    b = set(b)
    return [c for c in a if c not in b]

assert array_diff([1, 2], [1]) == [2]
assert array_diff([1, 2, 2], [1]) == [2, 2]
assert array_diff([1, 2, 2], [2]) == [1]
assert array_diff([1, 2, 2], []) == [1, 2, 2]
assert array_diff([], [1, 2]) == []
