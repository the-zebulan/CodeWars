from collections import defaultdict, Counter


def count_sel(nums):
    cnt = Counter(nums)
    d = defaultdict(list)
    total = 0
    unique = 0
    for k, v in cnt.iteritems():
        d[v].append(k)
        total += v
        unique += 1
    maximum = max(d)
    return [total, unique, len(d[1]), [sorted(d[maximum]), maximum]]

assert count_sel([-3, -2, -1, 3, 4, -5, -5, 5, -1, -5]) \
    == [10, 7, 5, [[-5], 3]]
assert count_sel([5, -1, 1, -1, -2, 5, 0, -2, -5, 3]) \
    == [10, 7, 4, [[-2, -1, 5], 2]]
assert count_sel([-2, 4, 4, -2, -2, -1, 3, 5, -5, 5]) \
    == [10, 6, 3, [[-2], 3]]
assert count_sel([4, -5, 1, -5, 2, 4, -1, 4, -1, 1]) \
    == [10, 5, 1, [[4], 3]]
assert count_sel([4, 4, 2, -3, 1, 4, 3, 2, 0, -5, 2, -2, -2, -5]) \
    == [14, 8, 4, [[2, 4], 3]]
