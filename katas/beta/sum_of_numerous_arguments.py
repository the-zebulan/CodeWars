def find_sum(*args):
    total = 0
    for a in args:
        if a < 0:
            return -1
        total += a
    return total
