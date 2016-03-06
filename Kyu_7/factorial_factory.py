def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    return reduce(lambda a, b: a * b, xrange(1, n + 1))
