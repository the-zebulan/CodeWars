def bar_triang(*args):
    return map(lambda a: round(sum(a) / 3.0, 4), zip(*args))
