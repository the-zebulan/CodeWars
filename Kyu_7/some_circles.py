from math import pi

OUTPUT = 'We have this much circle: {:.0f}'.format


def sum_circles(*args):
    return OUTPUT(sum(pi * (diameter / 2.0) ** 2 for diameter in args))
