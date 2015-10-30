from math import ceil

SUFFIX = {1: 'st', 2: 'nd', 3: 'rd'}


def whatCentury(year):
    """ what_century == PEP8, forced mixedCase by CodeWars """
    century = int(ceil(int(year) / 100.0))
    quo, rem = divmod(century, 10)
    if quo == 1 and 1 <= rem <= 3:
        suffix = 'th'
    else:
        suffix = SUFFIX.get(rem, 'th')
    return '{}{}'.format(century, suffix)


assert whatCentury('1999') == '20th'
assert whatCentury('2011') == '21st'
assert whatCentury('2154') == '22nd'
assert whatCentury('2259') == '23rd'
assert whatCentury('1124') == '12th'
assert whatCentury('2000') == '20th'
assert whatCentury('1234') == '13th'
assert whatCentury('2000') == '20th'
