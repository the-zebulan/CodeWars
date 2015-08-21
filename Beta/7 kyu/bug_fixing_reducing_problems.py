def calculate_total(t1, t2):
    return sum(t1) > sum(t2)

assert calculate_total([1, 2, 2], [1, 0, 0]) is True
assert calculate_total([6, 45, 1], [1, 55, 0]) is False
assert calculate_total([57, 2, 1], []) is True
assert calculate_total([], [3, 4, 3]) is False
assert calculate_total([], []) is False
