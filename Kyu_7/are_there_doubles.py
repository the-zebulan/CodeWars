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


assert double_check("abca") is False
assert double_check("aabc") is True
assert double_check("a 11 c d") is True
assert double_check("AabBcC") is True
assert double_check("a b  c") is True
assert double_check("a b c d e f g h i h k") is False
