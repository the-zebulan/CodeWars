def fill_gaps(lst):
    none_cnt = 0
    prev = None
    result = []
    for i, a in enumerate(lst):
        print 'i: {}\tprev: {}\t\ta: {}'.format(i, prev, a)
        if a is None:
            none_cnt += 1
            continue
        if a == prev:
            result.extend([a] * (none_cnt + 2))
            none_cnt = 0
        else:
            result.extend([prev] + [None] * none_cnt + [a])
            none_cnt = 0
        prev = a

    print result


# print fill_gaps([1, None, 1])  # == [1,1,1]
# print fill_gaps([1, None, None, None, 1])  # == [1,1,1,1,1]
print fill_gaps([1, None, 1, 2, None, 2])  # == [1,1,1,2,2,2]
print fill_gaps([1, None, 2, None, 2, None, 1])  # == [1,None,2,2,2,None,1]
print fill_gaps([1, None, 2])  # == [1,None,2]
print fill_gaps([None, 1, None])  # == [None,1,None]
print fill_gaps(['codewars', None, None, 'codewars', 'real work', None, None,
                 'real work'])  # == ["codewars", "codewars", "codewars", "codewars", "real work", "real work", "real work", "real work"]
