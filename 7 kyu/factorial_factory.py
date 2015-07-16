def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    return reduce(lambda a, b: a * b, xrange(1, n + 1))

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(-2) is None
