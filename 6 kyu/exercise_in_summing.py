def maximum_sum(values, n):
    if not values or n <= 0:
        return 0
    length = len(values)
    if n > length:
        n = length
    values.sort()
    return sum(values[-n:])


def minimum_sum(values, n):
    if not values or n <= 0:
        return 0
    length = len(values)
    if n > length:
        n = length
    values.sort()
    return sum(values[:n])

assert minimum_sum([5, 4, 3, 2, 1], 2) == 3
assert maximum_sum([5, 4, 3, 2, 1], 3) == 12
