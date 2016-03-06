def eq_sum_powdig(hMax, exp):
    return [a for a in xrange(2, hMax + 1)
            if a == sum(int(b) ** exp for b in str(a))]
