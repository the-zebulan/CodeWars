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
