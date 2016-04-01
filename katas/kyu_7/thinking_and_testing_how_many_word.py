# from itertools import cycle
#
# WORD = 'word'
#
#
# def testit(s):
#     cycled_word = cycle(WORD)
#     current = next(cycled_word)
#     result = 0
#     for letter in s.lower():
#         if current == letter:
#             current = next(cycled_word)
#             result += 1
#     return result / len(WORD)


# inspired by a solution on CodeWars by Unnamed
from re import compile, finditer, I

REGEX = compile(r'w.*?o.*?r.*?d', flags=I)


def testit(s):
    return sum(bool(a) for a in finditer(REGEX, s))
