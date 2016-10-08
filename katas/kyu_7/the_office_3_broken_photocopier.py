from string import maketrans, translate


def broken(inp):
    return translate(inp, maketrans('01', '10'))
