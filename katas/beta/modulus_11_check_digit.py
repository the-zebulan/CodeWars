from itertools import cycle


def add_check_digit(s):
    rem = 11 - sum(int(a) * b for a, b in zip(
        reversed(s), cycle(xrange(2, 8)))) % 11
    return '{}{}'.format(s, {10: 'X', 11: 0}.get(rem, rem))
