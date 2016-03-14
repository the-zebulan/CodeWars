def average(x):
    return sum(x) / len(x) if not isinstance(x, str) else 'Incorrect'
