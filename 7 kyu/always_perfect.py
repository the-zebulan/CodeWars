from math import modf


def check_root(string):
    numbers = string.split(',')
    if not len(numbers) == 4:
        return 'incorrect input'
    try:
        total = reduce(lambda a, b: a * b, (int(c) for c in numbers)) + 1
        f, i = modf(total ** 0.5)  # fractional, integer
        return 'not consecutive' if f else '{}, {}'.format(total, int(i))
    except ValueError:
        return 'incorrect input'

assert check_root('4,5,6,7') == '841, 29'
assert check_root('3,s,5,6') == 'incorrect input'
assert check_root('11,13,14,15') == 'not consecutive'
assert check_root('10,11,12,13,15') == 'incorrect input'
assert check_root('10,11,12,13') == '17161, 131'
