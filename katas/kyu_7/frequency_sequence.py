from collections import Counter


def freq_seq(s, sep):
    cnt = Counter(s)
    return sep.join(str(cnt[a]) for a in s)
