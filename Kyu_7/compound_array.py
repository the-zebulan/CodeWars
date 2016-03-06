from itertools import izip_longest


def compound_array(a, b):
    result = []
    for c, d in izip_longest(a, b):
        if c is not None:
            result.append(c)
        if d is not None:
            result.append(d)
    return result
