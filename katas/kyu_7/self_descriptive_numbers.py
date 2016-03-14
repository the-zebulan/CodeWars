from collections import Counter


def self_descriptive(num):
    s = [int(a) for a in str(num)]
    cnt = Counter(s)
    return all(cnt[i] == b for i, b in enumerate(s))
