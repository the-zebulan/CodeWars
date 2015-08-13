def types(x):
    return type(x).__name__
    # result = str(type(x))
    # return result[result.find('\'') + 1:-2]

assert types(10) == 'int'
assert types(9.7) == 'float'
assert types('&*(') == 'str'
assert types(True) == 'bool'
