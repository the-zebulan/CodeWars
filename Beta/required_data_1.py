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
