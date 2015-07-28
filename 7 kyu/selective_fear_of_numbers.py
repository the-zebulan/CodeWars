DAYS = {'Monday': lambda a: a == 12,
        'Tuesday': lambda b: b > 95,
        'Wednesday': lambda c: c == 34,
        'Thursday': lambda d: d == 34,
        'Friday': lambda e: e % 2 == 0,
        'Saturday': lambda f: f == 56,
        'Sunday': lambda g: abs(g) == 666}


def am_I_afraid(day, num):
    """ am_i_afraid == PEP8, forced camelCase by CodeWars """
    return DAYS[day](num)

assert am_I_afraid("Monday", 13) is False
assert am_I_afraid("Sunday", -666) is True
assert am_I_afraid("Tuesday", 2) is False
assert am_I_afraid("Tuesday", 965) is True
assert am_I_afraid("Friday", 2) is True
