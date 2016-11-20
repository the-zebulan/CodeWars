def hor_mirror(s):
    return '\n'.join(reversed(s.split('\n')))


def vert_mirror(s):
    return '\n'.join(a[::-1] for a in s.split('\n'))


def oper(fct, s):
    return fct(s)
