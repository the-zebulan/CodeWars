from re import compile, sub

REGEX = compile(r'\b[yY][oO][uU]+\b|\b[uU]\b')


def autocorrect(string):
    return sub(REGEX, 'your sister', string)

assert autocorrect('u') == 'your sister'
assert autocorrect('you') == 'your sister'
assert autocorrect('Youuuuu') == 'your sister'
assert autocorrect('youtube') == 'youtube'
assert autocorrect('You u youville utube you youyouyou uuu '
                   'raiyou united youuuu u you') == \
    'your sister your sister youville utube your sister youyouyou uuu ' \
    'raiyou united your sister your sister your sister'
