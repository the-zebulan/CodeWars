from itertools import cycle


def add_check_digit(s):
    rem = 11 - sum(int(a) * b for a, b in zip(
        reversed(s), cycle(xrange(2, 8)))) % 11
    return '{}{}'.format(s, {10: 'X', 11: 0}.get(rem, rem))


assert add_check_digit('111111111') == '1111111118'
assert add_check_digit('12388878') == '123888782'
assert add_check_digit('036532') == '0365327'
assert add_check_digit('9735597355') == '97355973550'
