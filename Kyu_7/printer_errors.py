COLORS = set('abcdefghijklm')


def printer_error(s):
    errors = 0
    for i, color in enumerate(s, 1):
        if color not in COLORS:
            errors += 1
    else:
        return '{}/{}'.format(errors, i)
