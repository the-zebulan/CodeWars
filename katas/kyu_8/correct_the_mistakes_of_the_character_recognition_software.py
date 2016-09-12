from string import maketrans, translate


def correct(s):
    return translate(s, maketrans('501', 'SOI'))
