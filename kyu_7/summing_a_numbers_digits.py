def sumDigits(number):
    """ sum_digits == PEP8 (camelCase forced by CodeWars) """
    return sum(map(int, str(abs(number))))
