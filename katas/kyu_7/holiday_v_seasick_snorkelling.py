from operator import truediv


def sea_sick(s):
    result = sum(s[a:a + 2] in '_~_' for a in xrange(len(s) - 1))
    if truediv(result, len(s)) > 0.2:
        return 'Throw Up'
    return 'No Problem'
