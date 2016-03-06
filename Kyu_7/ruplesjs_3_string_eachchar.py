def each_char(s, arg):
    if isinstance(arg, str):
        return ''.join('{}{}'.format(a, arg) for a in s)
    return ''.join(arg(b) for b in s)
