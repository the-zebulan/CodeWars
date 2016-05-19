def compose(f, g):
    return lambda *args: f(g(*args))
