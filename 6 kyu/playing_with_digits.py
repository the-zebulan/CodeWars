def dig_pow(n, p):
    total = sum(int(a) ** i for i, a in enumerate(str(n), start=p))
    quo, rem = divmod(total, n)
    return quo if rem == 0 else -1

assert dig_pow(695, 2) == 2
assert dig_pow(46288, 3) == 51
assert dig_pow(89, 1) == 1
assert dig_pow(92, 1) == -1
