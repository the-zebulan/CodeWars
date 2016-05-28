from itertools import cycle


def chessboard(s):
    n, m = (int(a) for a in s.split())
    star_dot = cycle('*.')
    row = ''.join(next(star_dot) for _ in xrange(m))
    rev = row[::-1]
    return '\n'.join(row if b % 2 == 0 else rev for b in xrange(n))
