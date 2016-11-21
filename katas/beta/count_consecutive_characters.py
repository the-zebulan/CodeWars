from itertools import groupby


def count_consecutives(s):
    return ''.join(str(sum(1 for _ in g)) + k for k, g in groupby(s))


# PEP8: kata should use snake_case instead of mixedCase
countConsecutives = count_consecutives
