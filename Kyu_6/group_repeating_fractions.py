from itertools import groupby


def repeating_fractions(numerator, denominator):
    integer, fractional = str(numerator / float(denominator)).split('.')
    grouped = []
    for k, g in groupby(fractional):
        try:
            next(g)
            next(g)
            grouped.append('({})'.format(k))
        except StopIteration:
            grouped.append(k)
    return '{}.{}'.format(integer, ''.join(grouped))

assert repeating_fractions(1, 1) == '1.0'
assert repeating_fractions(1, 2) == '0.5'
assert repeating_fractions(1, 3) == '0.(3)'
assert repeating_fractions(2, 888) == '0.(0)(2)5(2)5(2)5(2)5'
assert repeating_fractions(1554, 70) == '22.2'
assert repeating_fractions(11, 7) == '1.57142857143'
assert repeating_fractions(15, 7) == '2.14285714286'
assert repeating_fractions(32, 11) == '2.90909090909'
