OUTPUT = '{}{}'.format
VOWELS = 'aeiou'


def pig_latin(string):
    if not string.isalpha() or not string:
        return None
    string = string.lower()
    first_vowel = None
    for i, a in enumerate(string):
        if first_vowel is None and a in VOWELS:
            first_vowel = i
            break

    if first_vowel is None:
        return OUTPUT(string, 'ay')
    if first_vowel == 0:
        return OUTPUT(string, 'way')
    return OUTPUT(string[first_vowel:] + string[:first_vowel], 'ay')
