from collections import Counter


def first_dup(s):
    cnt = Counter(s)
    for a in s:
        if cnt[a] >= 2:
            return a
