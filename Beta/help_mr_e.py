from re import compile, sub

OUTPUT = '{}{}'.format
REGEX = compile(r'[^a-zA-Z0-9 ]')


def evenator(s):
    return ' '.join(OUTPUT(a, a[-1]) if len(a) % 2 else a
                    for a in sub(REGEX, '', s).split())


assert evenator('How did we end up here? We go?') == \
    'Howw didd we endd up here We go'
assert evenator('I got a hole in 1!') == 'II gott aa hole in 11'
