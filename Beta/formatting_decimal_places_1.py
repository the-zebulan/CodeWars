def two_decimal_places(n):
    return round(n, 2)


assert two_decimal_places(4.659725356) == 4.66
assert two_decimal_places(173735326.3783732637948948) == 173735326.38
assert two_decimal_places(4.653725356) == 4.65
