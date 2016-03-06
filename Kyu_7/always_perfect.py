from math import modf


def check_root(string):
    numbers = string.split(',')
    if not len(numbers) == 4:
        return 'incorrect input'
    try:
        total = reduce(lambda a, b: a * b, (int(c) for c in numbers)) + 1
        f, i = modf(total ** 0.5)  # fractional, integer
        return 'not consecutive' if f else '{}, {:.0f}'.format(total, i)
    except ValueError:
        return 'incorrect input'
