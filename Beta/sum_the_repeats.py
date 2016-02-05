from collections import defaultdict


def repeat_sum(lst):
    count = defaultdict(int)
    for a in lst:
        for b in set(a):
            count[b] += 1
    return sum(k for k, v in count.iteritems() if v > 1)


assert repeat_sum([[1, 2, 3], [2, 8, 9], [7, 123, 8]]) == 10  # 2 + 8
assert repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]) == 0
assert repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]) == 9  # 1 + 8
