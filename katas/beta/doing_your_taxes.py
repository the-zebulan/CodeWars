def tax(x):
    return x + x * 0.05 if not isinstance(x, str) else 'Error 404'
