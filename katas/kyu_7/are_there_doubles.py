from itertools import groupby


def double_check(s):
    return any(sum(1 for _ in g) == 2 for _, g in groupby(s.lower()))


# from re import compile, search
#
# REGEX = compile(r'(.)\1')
#
#
# def double_check(s):
#     return bool(search(REGEX, s.lower()))
