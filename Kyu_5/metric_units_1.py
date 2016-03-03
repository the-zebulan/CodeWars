PREFIXES = ((10 ** 24, 'Y'), (10 ** 21, 'Z'), (10 ** 18, 'E'),
            (10 ** 15, 'P'), (10 ** 12, 'T'), (10 ** 9, 'G'),
            (10 ** 6, 'M'), (10 ** 3, 'k'), (1, ''))


def meters(n):
    for value, prefix in PREFIXES:
        check = float(n) / value
        if int(check):
            return '{:g}{}m'.format(check, prefix)


assert meters(5) == '5m'
assert meters(51500) == '51.5km'
assert meters(5000000) == '5Mm'
assert meters(999) == '999m'
assert meters(123456) == '123.456km'
assert meters(600) == '600m'
assert meters(9e+24) == '9Ym'
assert meters(400000000000000000000000) == '400Zm'
assert meters(7000000000000000000000000) == '7Ym'
assert meters(9000000000.0)
