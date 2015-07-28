VALID = {'8', 'W', 'T', 'Y', 'U', 'I', 'O', 'A', 'H', 'X', 'V', 'M'}


def owl_pic(text):
    string = ''.join(a for a in text.upper() if a in VALID)
    return '{}\'\'0v0\'\'{}'.format(string, string[::-1])

assert owl_pic('xwe') == "XW''0v0''WX"
assert owl_pic("kuawd6r8q27y87t93r76352475437") == "UAW8Y8T''0v0''T8Y8WAU"
assert owl_pic("t6ggggggggWw") == "TWW''0v0''WWT"
