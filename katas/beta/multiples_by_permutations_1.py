def search_permMult(n_max, k):
    """ search_perm_mult == PEP8 (forced mixedCase by Codewars) """
    return sum(sorted(str(a)) == sorted(str(a * k))
               for a in xrange(1, n_max / k))
