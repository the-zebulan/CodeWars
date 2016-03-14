from math import pi


def circleArea(r):
    """ circle_area == PEP8 (forced camelCase by codewars) """
    if r <= 0 or not isinstance(r, (int, float)):
        return False
    return round(pi * (r ** 2), 2)
