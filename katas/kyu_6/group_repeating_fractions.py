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
