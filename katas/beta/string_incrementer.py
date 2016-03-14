from re import compile, search

REGEX = compile(r'(?P<num>\d+)$')


def increment_string(strng):
    m = search(REGEX, strng)
    if m:
        num = m.group('num')
        return '{}{:0>{}}'.format(strng[:m.start()], int(num) + 1, len(num))
    return '{}1'.format(strng)
