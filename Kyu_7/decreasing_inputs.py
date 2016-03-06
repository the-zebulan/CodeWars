def add(*args):
    return round(sum(a / float(i) for i, a in enumerate(args, start=1)))
