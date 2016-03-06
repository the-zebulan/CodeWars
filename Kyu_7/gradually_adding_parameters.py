def add(*args):
    return sum(i * a for i, a in enumerate(args, start=1))
