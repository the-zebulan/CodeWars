from math import pi


def circleArea(r):
    """ circle_area == PEP8 (forced camelCase by codewars) """
    if r <= 0 or not isinstance(r, (int, float)):
        return False
    return round(pi * (r ** 2), 2)

assert circleArea(-1485.86) is False
assert circleArea(0) is False
assert circleArea(43.2673) == 5881.25
assert circleArea(68) == 14526.72
assert circleArea("number") is False
