from re import compile, findall

REGEX = compile(r'(?=1(0+)1)')


def gap(num):
    return max(len(a) for a in findall(REGEX, bin(num)) + [''])
