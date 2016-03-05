from string import ascii_uppercase

AZ = dict(zip(ascii_uppercase, xrange(1, 27)))


def product_mod_47(seq):
    return reduce(lambda a, b: a * b, (AZ[c] for c in seq)) % 47


def ride(group, comet):
    return 'GO' if product_mod_47(group) == product_mod_47(comet) else 'STAY'
