from string import ascii_uppercase

AZ = dict(zip(ascii_uppercase, map(str, xrange(1, 27))))


def alphabet_position(text):
    return ' '.join(AZ[a] for a in text.upper() if a.isalpha())
