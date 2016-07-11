def hollow_Triangle(n):
    """ hollow_triangle == PEP8 (forced by Codewars) """
    width = n * 2 - 1
    row = '{{:_^{}}}'.format(width).format
    return [row(mid(a)) for a in xrange(1, width, 2)] + [width * '#']


def mid(n):
    return '#' if n == 1 else '#{}#'.format('_' * (n - 2))
