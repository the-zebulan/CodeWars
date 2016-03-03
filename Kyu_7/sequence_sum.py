def sum_of_n(n):
    last = 0
    is_positive = n > 0
    result = [0]
    for a in xrange(1, abs(n) + 1):
        last += a
        result.append(last if is_positive else last * -1)
    return result

assert sum_of_n(3) == [0, 1, 3, 6]
assert sum_of_n(1) == [0, 1]
assert sum_of_n(0) == [0]
assert sum_of_n(-4) == [0, -1, -3, -6, -10]
