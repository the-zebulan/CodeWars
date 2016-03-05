from string import maketrans, ascii_lowercase as low, ascii_uppercase as up

TRANSLATION = maketrans(up + low, up[::-1] + low[::-1])


def decode(string):
    return string.translate(TRANSLATION) \
        if isinstance(string, str) else 'Input is not a string'
