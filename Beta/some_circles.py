from math import pi

OUTPUT = 'We have this much circle: {:.0f}'.format


def sum_circles(*args):
    return OUTPUT(sum(pi * (diameter / 2.0) ** 2 for diameter in args))

assert sum_circles(2) == 'We have this much circle: 3'
assert sum_circles(2, 3, 4) == 'We have this much circle: 23'
assert sum_circles(48, 7, 8, 9, 10) == 'We have this much circle: 2040'
assert sum_circles(1) == 'We have this much circle: 1'
assert sum_circles(1, 1, 1, 2, 3, 4, 5) == 'We have this much circle: 45'
