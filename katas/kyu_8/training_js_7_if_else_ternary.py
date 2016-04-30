def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)
