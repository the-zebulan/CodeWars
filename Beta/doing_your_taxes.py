def tax(x):
    return x + x * 0.05 if not isinstance(x, str) else 'Error 404'

assert tax(1.2) == 1.26
assert tax(100) == 105
assert tax("Hello") == "Error 404"
