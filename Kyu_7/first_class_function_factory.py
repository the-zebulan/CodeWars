def factory(x):
    return lambda b: map(lambda a: a * x, b)
