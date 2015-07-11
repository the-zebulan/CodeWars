def lcm(*args):
    """Compute the least common multiple of some non-negative integers"""
    args = set(args)  # remove duplicates
    if 0 in args:
        return 0
    x = max(args)
    y = x
    args.remove(x)
    while any(x % z for z in args):
        x += y
    return x

assert lcm(2, 5) == 10
assert lcm(2, 3, 4) == 12
assert lcm(9) == 9
assert lcm(0) == 0
assert lcm(0, 1) == 0
