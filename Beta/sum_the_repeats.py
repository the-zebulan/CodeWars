from collections import defaultdict


def repeat_sum(lst):
    count = defaultdict(int)
    for a in lst:
        for b in set(a):
            count[b] += 1
    return sum(k for k, v in count.iteritems() if v > 1)
