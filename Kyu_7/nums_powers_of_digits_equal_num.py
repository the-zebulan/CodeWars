def eq_sum_powdig(hMax, exp):
    return [a for a in xrange(2, hMax + 1)
            if a == sum(int(b) ** exp for b in str(a))]


assert eq_sum_powdig(100, 2) == []
assert eq_sum_powdig(1000, 2) == []
assert eq_sum_powdig(200, 3) == [153]
assert eq_sum_powdig(370, 3) == [153, 370]
