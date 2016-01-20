def sel_quot(arr, m, dir_str=None):
    uniq = sorted(set(arr))
    length = len(uniq)
    result = set()
    for a in xrange(length - 1):
        denominator = uniq[a]
        for b in xrange(a + 1, length):
            numerator = uniq[b]
            q, r = divmod(numerator, denominator)
            if not r and q >= m:
                result.add((q, (numerator, denominator)))
    if dir_str is None:
        return sorted(result)
    if dir_str.lower() == 'odd':
        return sorted(c for c in result if c[0] % 2)
    return sorted(d for d in result if not d[0] % 2)


arr = [2, 4, 27, 16, 9, 15, 25, 6, 12, 83, 24, 49, 7, 5, 94, 12, 6]
assert sel_quot(arr, 6, 'Odd') == [(7, (49, 7)), (47, (94, 2))]
assert sel_quot(arr, 6, 'even') == \
    [(6, (12, 2)), (6, (24, 4)), (8, (16, 2)), (12, (24, 2))]
assert sel_quot(arr, 6) == \
    [(6, (12, 2)), (6, (24, 4)), (7, (49, 7)),
     (8, (16, 2)), (12, (24, 2)), (47, (94, 2))]
