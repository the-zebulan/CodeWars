import math

DEGREES_PER_RADIAN = math.pi / 180.0
RADIANS_PER_DEGREE = 180.0 / math.pi
OUTPUT = '{:g}{}'.format

math.degrees = lambda rad: OUTPUT(round(RADIANS_PER_DEGREE * rad, 2), 'deg')
math.radians = lambda deg: OUTPUT(round(DEGREES_PER_RADIAN * deg, 2), 'rad')
