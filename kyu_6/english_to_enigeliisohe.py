VOWELS = 'aeiou'
PREV_VOWEL = {'b': 'a', 'c': 'a', 'd': 'a', 'f': 'e', 'g': 'e', 'h': 'e',
              'j': 'i', 'k': 'i', 'l': 'i', 'm': 'i', 'n': 'i', 'p': 'o',
              'q': 'o', 'r': 'o', 's': 'o', 't': 'o', 'v': 'u', 'w': 'u',
              'x': 'u', 'y': 'u', 'z': 'u'}


def toexuto(text):
    result = []
    for a in text:
        low = a.lower()
        if a.isalpha() and low not in VOWELS:
            result.append('{}{}'.format(a, PREV_VOWEL[low]))
        else:
            result.append(a)
    return ''.join(result)
