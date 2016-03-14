VOWELS = set('AEIOUY')


def strip_vowels(s):
    return ''.join(a for a in s if a not in VOWELS)


def vanity_plate(plate):
    up = plate.upper()
    if len(up) <= 8:
        return up

    no_vowels = ' '.join('{}{}{}'.format(b[0], strip_vowels(b[1:-1]), b[-1])
                         if len(b) > 1 else b for b in up.split())
    if len(no_vowels) <= 8:
        return no_vowels

    no_spaces = no_vowels.replace(' ', '')
    if len(no_spaces) <= 8:
        return no_spaces

    first_letters = ''.join(c[0] for c in up.split())
    if len(first_letters) <= 8:
        return first_letters
    return ''
