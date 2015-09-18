def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m

assert paperwork(5, 5) == 25
assert paperwork(-2, 10) == 0
