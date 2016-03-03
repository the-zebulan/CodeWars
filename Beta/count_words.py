from re import compile, finditer

OMIT = {'a', 'the', 'on', 'at', 'of', 'upon', 'in', 'as'}
REGEX = compile(r'[a-z]+')


def word_count(s):
    return sum(a.group() not in OMIT for a in finditer(REGEX, s.lower()))
