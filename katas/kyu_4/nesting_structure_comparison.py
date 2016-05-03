def nones(itr):
    return [nones(a) if isinstance(a, (list, tuple)) else None for a in itr]


def same_structure_as(a, b):
    return nones(a) == nones(b) if type(a) == type(b) else False
