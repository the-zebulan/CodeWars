from itertools import cycle, islice


def chessboard(s):
    n, m = (int(a) for a in s.split())
    if not n or not m:
        return ''
    return '\n'.join(islice(cycle(
        (''.join(islice(cycle('*.'), m)), ''.join(islice(cycle('.*'), m)))
    ), n))
