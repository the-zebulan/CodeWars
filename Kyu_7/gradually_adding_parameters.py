def add(*args):
    return sum(i * a for i, a in enumerate(args, start=1))

# add = lambda *args: sum(i * a for i, a in enumerate(args, start=1))

assert add() == 0
assert add(100, 200, 300) == 1400
assert add(2) == 2
