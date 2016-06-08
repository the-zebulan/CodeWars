from itertools import cycle


def chessboard(s):
    n, m = (int(a) for a in s.split())
    if not m:
        return ''
    star_dot = cycle('*.')
    row = ''.join(next(star_dot) for _ in xrange(m))
    if m % 2 == 0:
        next(star_dot)
    row2 = ''.join(next(star_dot) for _ in xrange(m))
    return '\n'.join(row if b % 2 == 0 else row2 for b in xrange(n))
