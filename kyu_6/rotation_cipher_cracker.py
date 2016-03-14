from string import ascii_lowercase as az, maketrans

TRANSLATIONS = [maketrans(az, az[a:] + az[:a]) for a in xrange(1, 26)]


def decode(msg, contents):
    result = []
    for b in TRANSLATIONS:
        tmp = msg.translate(b)
        if contents in tmp:
            result.append(tmp)
    return result
