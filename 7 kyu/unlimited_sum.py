def sum(*args):
    return reduce(lambda a, b: a + b, (c for c in args if isinstance(c, int)))
