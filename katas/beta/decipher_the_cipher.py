from string import ascii_lowercase as az

OPPOSITES = dict(zip(az, reversed(az)))


def encrypter(strng):
    return ''.join(OPPOSITES.get(a, a) for a in strng.encode('rot13'))
