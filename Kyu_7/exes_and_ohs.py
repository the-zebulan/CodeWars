VALUES = {'x': 1, 'X': 1, 'o': -1, 'O': -1}


def xo(s):
    return not sum(VALUES.get(a, 0) for a in s)
