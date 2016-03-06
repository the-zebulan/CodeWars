def isLeapYear(year):
    """ is_leap_year == PEP8, forced mixedCase by CodeWars """
    return year % 4 == 0 and not year % 100 == 0 or year % 400 == 0
