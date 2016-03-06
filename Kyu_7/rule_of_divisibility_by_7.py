def seven(m):
    steps = 0
    while m > 99:
        q, r = divmod(m, 10)
        m = q - (2 * r)
        steps += 1
    return m, steps
