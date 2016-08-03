def get_real_floor(n):
    return n - (1 if n < 13 else 2) if n > 0 else n
