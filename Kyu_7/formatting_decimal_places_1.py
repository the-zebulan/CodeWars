from math import trunc


def two_decimal_places(number):
    factor = float(10 ** 2)
    return trunc(number * factor) / factor


assert two_decimal_places(10.1289767789) == 10.12
assert two_decimal_places(-7488.83485834983) == -7488.83
assert two_decimal_places(4.653725356) == 4.65
