from math import ceil


def cooking_time(eggs):
    return ceil(eggs / 8.0) * 5

assert cooking_time(0) == 0
assert cooking_time(5) == 5
assert cooking_time(10) == 10
