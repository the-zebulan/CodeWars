# coding=utf-8
from re import escape, sub


def solution(s, markers):
    return s if not markers else \
        sub(r'( *[{}].*)'.format(escape(''.join(markers))), '', s)
