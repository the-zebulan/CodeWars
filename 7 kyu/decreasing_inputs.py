def add(*args):
    return round(sum(a / float(i) for i, a in enumerate(args, start=1)))

assert add(100, 200, 300) == 300
assert add(2) == 2
assert add(4, -3, -2) == 2
