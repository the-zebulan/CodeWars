def spoonerize(words):
    a, b = words.split()
    return '{}{} {}{}'.format(b[0], a[1:], a[0], b[1:])
