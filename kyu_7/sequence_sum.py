def sum_of_n(n):
    last = 0
    is_positive = n > 0
    result = [0]
    for a in xrange(1, abs(n) + 1):
        last += a
        result.append(last if is_positive else last * -1)
    return result
