def persistence(n):
    cnt = 0
    n = str(n)
    while len(n) > 1:
        n = str(reduce(lambda a, b: a * b, (int(c) for c in n)))
        cnt += 1
    return cnt
