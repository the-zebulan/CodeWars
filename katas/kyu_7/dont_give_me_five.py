def dont_give_me_five(start, stop):
    return sum('5' not in str(a) for a in xrange(start, stop + 1))
