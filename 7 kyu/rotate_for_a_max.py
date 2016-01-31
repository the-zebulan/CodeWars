def max_rot(n):
    maximum = n
    s = list(str(n))
    for i in xrange(len(s) - 1):
        s.append(s.pop(i))
        current = int(''.join(s))
        if current > maximum:
            maximum = current
    return maximum


assert max_rot(56789) == 68957
assert max_rot(38458215) == 85821534
assert max_rot(195881031) == 988103115
assert max_rot(896219342) == 962193428
assert max_rot(69418307) == 94183076
