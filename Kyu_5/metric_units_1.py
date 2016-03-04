PREFIXES = ((10 ** 24, 'Y'), (10 ** 21, 'Z'), (10 ** 18, 'E'),
            (10 ** 15, 'P'), (10 ** 12, 'T'), (10 ** 9, 'G'),
            (10 ** 6, 'M'), (10 ** 3, 'k'), (1, ''))


def meters(n):
    for value, prefix in PREFIXES:
        check = float(n) / value
        if int(check):
            return '{:g}{}m'.format(check, prefix)
