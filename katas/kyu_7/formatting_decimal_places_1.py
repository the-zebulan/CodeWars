from math import trunc


def two_decimal_places(number):
    factor = float(10 ** 2)
    return trunc(number * factor) / factor
