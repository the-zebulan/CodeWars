def merge_by_n(lst, lst2, n):
    iter1 = iter(lst)
    result = []
    for a in lst2:
        result.extend((next(iter1) for _ in xrange(n - 1)))
        result.append(a)
    result.extend(iter1)
    return result


assert merge_by_n(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                  ['X', 'Y'], 3) == \
    ['a', 'b', 'X', 'c', 'd', 'Y', 'e', 'f', 'g', 'h']

print merge_by_n(list('abc'), list('XYZ'), 2)
print merge_by_n([], ['a'], 2)
