def isLeapYear(year):
    """ is_leap_year == PEP8, forced mixedCase by CodeWars """
    return year % 4 == 0 and not year % 100 == 0 or year % 400 == 0

assert isLeapYear(1984) is True
assert isLeapYear(2000) is True
assert isLeapYear(1234) is False
assert isLeapYear(1100) is False
