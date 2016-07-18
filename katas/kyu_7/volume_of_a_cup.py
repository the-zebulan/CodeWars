from math import pi


def cup_volume(top, bottom, height):
    r1 = top / 2.0
    r2 = bottom / 2.0
    return round((1 / 3.0 * pi) * (r1 ** 2 + r1 * r2 + r2 ** 2) * height, 2)
