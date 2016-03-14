def nb_dig(n, d):
    return ''.join(str(a ** 2) for a in xrange(n + 1)).count(str(d))
