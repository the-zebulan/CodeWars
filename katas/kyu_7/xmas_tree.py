from itertools import chain


def xMasTree(n):
    width = n * 2 - 1
    row = '{{:_^{}}}'.format(width).format
    return [row(a * '#') for a in chain(xrange(1, width + 1, 2), (1, 1))]
