from re import split

OUTPUT = '{}{}{}'.format


def abbreviate(string):
    result = []
    for a in split(r'(\W+)', string):
        length = len(a)
        result.append(a if length < 4 else OUTPUT(a[0], length - 2, a[-1]))
    return ''.join(result)

    # return ''.join(a if len(a) < 4 else OUTPUT(a[0], len(a) - 2, a[-1])
    #                for a in split(r'(\W+)', string))

assert abbreviate(
    'balloon: double-barreled, sat\'mat: sits, a-on, mat\'the, ') \
       == 'b5n: d4e-b6d, sat\'mat: s2s, a-on, mat\'the, '
assert abbreviate("internationalization") == "i18n"
assert abbreviate("accessibility") == "a11y"
assert abbreviate("Accessibility") == "A11y"
assert abbreviate('elephant-ride') == 'e6t-r2e'
