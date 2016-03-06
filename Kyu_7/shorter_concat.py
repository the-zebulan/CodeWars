def shorter_reverse_longer(a, b):
    if len(a) >= len(b):
        b, a = a, b
    return '{0}{1}{0}'.format(a, b[::-1])
