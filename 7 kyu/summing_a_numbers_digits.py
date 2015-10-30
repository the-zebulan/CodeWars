def sumDigits(number):
    """ sum_digits == PEP8 (camelCase forced by CodeWars) """
    return sum(map(int, str(abs(number))))

assert sumDigits(10) == 1
assert sumDigits(99) == 18
assert sumDigits(-32) == 5
