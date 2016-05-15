def make_lazy(func, *args, **kwargs):
    return lambda: func(*args, **kwargs)
