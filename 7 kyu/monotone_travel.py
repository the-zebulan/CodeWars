is_monotone = lambda heights: sorted(heights) == heights

assert is_monotone(range(1, 11)) is True
assert is_monotone([5,5,5,5,5,5,5]) is True
assert is_monotone([]) is True
assert is_monotone([1]) is True
assert is_monotone(range(5, 0, -1)) is False
assert is_monotone(range(5, -40, -1)) is False
