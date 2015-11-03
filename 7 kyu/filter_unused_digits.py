DIGITS = set('0123456789')


def unused_digits(*args):
    return ''.join(sorted(DIGITS.difference(''.join(str(a) for a in args))))

assert unused_digits(12, 34, 56, 78) == '09'
assert unused_digits(2015, 8, 26) == '3479'
assert unused_digits(276, 575) == '013489'
assert unused_digits(643) == '0125789'
assert unused_digits(864, 896, 744) == '01235'
