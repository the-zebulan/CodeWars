def maximum_sum(values, n):
    values.sort()
    return sum(values[-n:])


def minimum_sum(values, n):
    values.sort()
    return sum(values[:n])
