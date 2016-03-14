from string import ascii_uppercase

VALID = set(ascii_uppercase + ' !')


def rad_ladies(name):
    return ''.join(a for a in name.upper() if a in VALID)
