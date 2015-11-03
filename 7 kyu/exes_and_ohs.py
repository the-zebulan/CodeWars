VALUES = {'x': 1, 'X': 1, 'o': -1, 'O': -1}


def xo(s):
    return not sum(VALUES.get(a, 0) for a in s)

assert xo('xo') is True
assert xo('xo0') is True
assert xo('xxxoo') is False
