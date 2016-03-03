LITRES_PER_GALLON = 4.54609188
KILOMETERS_PER_MILE = 1.609344


def converter(mpg):
    return round(mpg * KILOMETERS_PER_MILE / LITRES_PER_GALLON, 2)

assert converter(12) == 4.25
assert converter(24) == 8.50
assert converter(36) == 12.74
