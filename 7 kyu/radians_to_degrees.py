import math

DEGREES_PER_RADIAN = math.pi / 180.0
RADIANS_PER_DEGREE = 180.0 / math.pi


def calculate(constant, variable, output):
    result = round(constant * variable, 2)
    r_int = int(result)
    return '{}{}'.format(r_int if result == r_int else result, output)

math.degrees = lambda rad: calculate(RADIANS_PER_DEGREE, rad, 'deg')
math.radians = lambda deg: calculate(DEGREES_PER_RADIAN, deg, 'rad')

assert math.degrees(math.pi) == '180deg'
assert math.radians(180) == '3.14rad'
