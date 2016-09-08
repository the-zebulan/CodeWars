from itertools import izip_longest


def solution(s):
    return [''.join(a) for a in izip_longest(s[::2], s[1::2], fillvalue='_')]
