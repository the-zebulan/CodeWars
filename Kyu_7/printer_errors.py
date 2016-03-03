COLORS = set('abcdefghijklm')


def printer_error(s):
    errors = 0
    for i, color in enumerate(s, 1):
        if color not in COLORS:
            errors += 1
    else:
        return '{}/{}'.format(errors, i)


assert printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbb'
                     'mmmmmmmmmmmmmmmmmmmxyz') == '3/56'
assert printer_error('aaabbbbhaijjjm') == '0/14'
assert printer_error('aaaxbbbbyyhwawiwjjjwwm') == '8/22'
