def dig_pow(n, p):
    total = sum(int(a) ** i for i, a in enumerate(str(n), start=p))
    quo, rem = divmod(total, n)
    return quo if rem == 0 else -1
