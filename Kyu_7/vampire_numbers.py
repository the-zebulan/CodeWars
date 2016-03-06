def vampire_test(x, y):
    return sorted(str(x * y)) == sorted('{}{}'.format(x, y))
