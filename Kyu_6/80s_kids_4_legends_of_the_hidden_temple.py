from itertools import chain


def mark_spot(n):
    if not (isinstance(n, int) and n % 2 and n > 0):
        return '?'
    result = []
    row_length = n * 2 - 1
    for a in chain(xrange(0, n, 2), xrange(n - 3, -1, -2)):
        row = [' '] * row_length
        row[a] = 'X'
        row[-(a + 1)] = 'X\n'
        result.append(''.join(row).rstrip(' '))
    return ''.join(result)


assert mark_spot(1) == 'X\n'
assert mark_spot(5) == 'X       X\n  X   X\n    X\n  X   X\nX       X\n'
assert mark_spot(11) == \
    'X                   X\n  X               X\n    X           X\n' \
    '      X       X\n        X   X\n          X\n        X   X\n' \
    '      X       X\n    X           X\n  X               X\n' \
    'X                   X\n'
assert mark_spot([]) == '?'
assert mark_spot('treasure') == '?'
assert mark_spot(-1) == '?'
