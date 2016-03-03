# def make_negative(number):
#     return number if number <= 0 else number * -1


def make_negative(number):
    return -abs(number)

assert make_negative(42) == -42
assert make_negative(-9) == -9
assert make_negative(0) == 0
