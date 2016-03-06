VALID = {'8', 'W', 'T', 'Y', 'U', 'I', 'O', 'A', 'H', 'X', 'V', 'M'}


def owl_pic(text):
    string = ''.join(a for a in text.upper() if a in VALID)
    return '{}\'\'0v0\'\'{}'.format(string, string[::-1])
