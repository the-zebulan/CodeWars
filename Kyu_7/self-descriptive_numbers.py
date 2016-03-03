from collections import Counter


def self_descriptive(num):
    s = [int(a) for a in str(num)]
    cnt = Counter(s)
    return all(cnt[i] == b for i, b in enumerate(s))


assert self_descriptive(21200) is True
assert self_descriptive(3211000) is True
assert self_descriptive(42101000) is True
assert self_descriptive(21230) is False
assert self_descriptive(11200) is False
assert self_descriptive(1210) is True
assert self_descriptive(51120111) is False
assert self_descriptive(2020) is True
assert self_descriptive(11201) is False
assert self_descriptive(6210001000) is True
