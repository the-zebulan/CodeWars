def find_sum(*args):
    total = 0
    for a in args:
        if a < 0:
            return -1
        total += a
    return total


assert find_sum(1, 3, 5) == 9
assert find_sum() == 0
assert find_sum(1, -2, 4) == -1
assert find_sum(0) == 0
assert find_sum(1, 1, 5) == 7
assert find_sum(1, 1, 1, 1, 1, 1, 1, 1, 0) == 8
assert find_sum(-1, -1, 5) == -1
assert find_sum(-1, -1, -5) == -1
assert find_sum(0, -1, 5) == -1
assert find_sum(0, 0, 0) == 0
