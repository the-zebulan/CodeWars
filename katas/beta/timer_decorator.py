from time import time
from functools import wraps


def timer(limit):
    def dec(func):
        @wraps(func)
        def time_func(*args, **kwargs):
            time_start = time()
            func(*args, **kwargs)
            return time() - time_start < limit
        return time_func
    return dec
