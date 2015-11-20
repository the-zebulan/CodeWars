# coding=utf-8
from re import escape, sub


def solution(s, markers):
    return s if not markers else \
        sub(r'( *[{}].*)'.format(escape(''.join(markers))), r'', s)


assert solution("apples, pears # and bananas\ngrapes\nbananas !apples",
                ["#", "!"]) == "apples, pears\ngrapes\nbananas"
assert solution('#', ['#', '!']) == ''
assert solution('\n§', ['#', '\xc2\xa7']) == '\n'
