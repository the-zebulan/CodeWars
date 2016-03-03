def persistence(n):
    cnt = 0
    n = str(n)
    while len(n) > 1:
        n = str(reduce(lambda a, b: a * b, (int(c) for c in n)))
        cnt += 1
    return cnt

assert persistence(39) == 3
assert persistence(4) == 0
assert persistence(25) == 2
assert persistence(999) == 4
