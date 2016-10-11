from string import maketrans, translate


def switcheroo(strng):
    return translate(strng, maketrans('ab', 'ba'))
