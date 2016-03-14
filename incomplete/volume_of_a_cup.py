from math import pi


def cup_volume(top, bottom, height):
    r1 = top / 2.0
    r2 = bottom / 2.0
    return round((1 / 3.0 * pi) * (r1 ** 2 + r1 * r2 + r2 ** 2) * height, 2)


assert cup_volume(1, 1, 1) == 0.79
assert cup_volume(10, 8, 10) == 638.79
assert cup_volume(1000, 1000, 1000) == 785398163.4
assert cup_volume(13.123, 123.12, 1) == 4436.57
assert cup_volume(5, 12, 31) == 1858.51
