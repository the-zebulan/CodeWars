def lstzip(a, b, fn):
    return [fn(*c) for c in zip(a, b)]
