DIGITS = set('0123456789')


def unused_digits(*args):
    return ''.join(sorted(DIGITS.difference(''.join(str(a) for a in args))))
