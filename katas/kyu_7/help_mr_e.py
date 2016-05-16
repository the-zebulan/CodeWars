from re import compile, sub

OUTPUT = '{}{}'.format
REGEX = compile(r'[^a-zA-Z0-9 ]')


def evenator(s):
    return ' '.join(OUTPUT(a, a[-1]) if len(a) % 2 else a
                    for a in sub(REGEX, '', s).split())
