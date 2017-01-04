from string import digits

VALID_CHARS = '$.' + digits


def remove_char(array):
    return [''.join(b for b in a if b in VALID_CHARS) for a in array]
